from datetime import datetime

import discord
from discord.activity import Game
from discord.ext import commands


class Leyley(commands.Bot):
    def __init__(self, **options) -> None:
        """
        Constructor for the Leyley bot
        """

        super().__init__(
            command_prefix="",
            activity=Game("with knives"),
            intents=discord.Intents.default(),
            **options,
        )

    def create_leyley_embed(self) -> discord.Embed:
        """
        Create Leyley themed embed

        :rtype: Embed
        :returns: The embed
        """

        embed = discord.Embed(
            color=discord.Color.dark_purple(), timestamp=datetime.now()
        )

        if self.user is not None:
            embed.set_footer(
                text=f"{self.user.name}#{self.user.discriminator}",
                icon_url=(self.user.avatar or self.user.default_avatar)
                .with_size(512)
                .url,
            )

        return embed
