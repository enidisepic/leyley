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
            **options
        )
