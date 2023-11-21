import calendar
import os
import time
from io import BytesIO

import discord
import jinja2
from discord import app_commands
from discord.ext import commands
from discord.interactions import Interaction
from html2image import Html2Image
from PIL import Image, ImageOps


class ImageCommands(commands.Cog):
    def __init__(self) -> None:
        project_root = os.path.realpath(os.path.curdir)

        self.__jinja_environment = jinja2.Environment(
            loader=jinja2.FileSystemLoader(os.path.join(project_root, "templates"))
        )

        self.__html2image = Html2Image(
            output_path="temp",
            custom_flags=[
                "--force-device-scale-factor=1.5",
                "--hide-scrollbars",
                "--disable-gpu",
            ],
            disable_logging=True,
            size=(1920, 1080),
        )

        temp_path = os.path.join(project_root, "temp")
        if not os.path.exists(temp_path):
            os.mkdir(temp_path)

        super().__init__()

    def __remove_transparency(self, path: str) -> BytesIO:
        """
        Removes the transparent background you get from Html2Image screenshots

        :param str path: The path to the image
        """

        image = Image.open(path)
        image = image.convert("RGB")

        image_inverted = ImageOps.invert(image)

        boundaries = image_inverted.getbbox(alpha_only=False)

        image = image.crop(boundaries)

        image_bytes = BytesIO()
        image.save(image_bytes, "png")
        image_bytes.seek(0)

        return image_bytes

    @app_commands.command(name="pass", description="Give someone the n-word pass")
    @app_commands.describe(member="The member who shall get the pass")
    async def n_word_pass(
        self, interaction: Interaction, member: discord.Member
    ) -> None:
        """
        Image generation command to give someone the n-word pass

        :param Interaction interaction: The Discord interaction
        """

        template = self.__jinja_environment.get_template("n_word_pass.j2")

        html_content = template.render(
            avatar_url=member.display_avatar.with_size(256).url,
            issuer=interaction.user.display_name,
            issuee=member.display_name,
        )

        image_filename = (
            f"{interaction.user.id}+{calendar.timegm(time.gmtime())}.png",
        )
        image_path = os.path.join("temp", image_filename[0])

        self.__html2image.screenshot(html_content, save_as=image_filename[0])

        cropped_image = self.__remove_transparency(image_path)

        os.remove(image_path)

        await interaction.response.send_message(
            f"{member.mention}! {interaction.user.mention} just gave you the n-word pass!",
            file=discord.File(cropped_image, "pass.png"),
        )
