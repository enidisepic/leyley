import discord
from discord import app_commands
from discord.ext import commands
from discord.interactions import Interaction

from leyley import Leyley


class UserCommands(commands.Cog):
    def __init__(self, bot: Leyley) -> None:
        """
        Constructor for the User commands cog

        :param Leyley bot: The bot object
        """

        self.__bot = bot

        super().__init__()

    @app_commands.command(name="avatar", description="Get someone's avatar")
    @app_commands.describe(user="The user who's avatar you want to get")
    @app_commands.describe(
        guild="Whether to return the guild specific avatar (if available) or global"
    )
    async def avatar(
        self, interaction: Interaction, user: discord.User, guild: bool = True
    ) -> None:
        embed = self.__bot.create_leyley_embed()

        embed.title = f"{user.display_name}'s avatar"

        if guild:
            avatar = user.display_avatar
        else:
            avatar = user.avatar or user.default_avatar

        embed.set_image(url=avatar.with_size(2048).url)

        await interaction.response.send_message(embed=embed)
