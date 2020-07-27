import asyncio

import config
import hoshino

bot = hoshino.init(config)
app = bot.asgi

if __name__ == '__main__':
    bot.run(
        host=config.HOST,
        port=config.PORT,
        debug=config.DEBUG,
        use_reloader=True,
        loop=asyncio.get_event_loop()
    )
