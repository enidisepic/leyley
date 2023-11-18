from discord.ext import commands
from loguru import logger

from leyley import Leyley


class Events(commands.Cog):
    def __init__(self, bot: Leyley) -> None:
        """
        Constructor for the event handler class

        :param Leyley bot: The bot
        """

        self.__bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        """
        Method to be ran when the bot is ready
        """

        if self.__bot.user is not None:
            logger.info(
                f"Logged in as {self.__bot.user.display_name} (@{self.__bot.user.name}#{self.__bot.user.discriminator})"
            )

        logger.info("Syncing commands")

        synced_commands = await self.__bot.tree.sync()
        synced_commands_length = len(synced_commands)

        if synced_commands_length:
            logger.info(f"Synced {synced_commands_length} commands")
