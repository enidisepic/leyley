import asyncio
import os

from events import Events
from image_commands import ImageCommands
from leyley import Leyley


async def main() -> None:
    """
    Main entrypoint for the Leyley bot
    """

    bot = Leyley()
    await bot.add_cog(Events(bot))
    await bot.add_cog(ImageCommands())

    await bot.start(os.getenv("LEYLEY_DISCORD_TOKEN") or "")


if __name__ == "__main__":
    asyncio.run(main())
