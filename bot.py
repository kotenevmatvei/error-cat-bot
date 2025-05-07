import configparser
import asyncio
from telegram import Bot
import os

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
BASE_URL = os.getenv("BASE_URL")

http_error_codes = [
    100, 101, 102, 103,
    200, 201, 202, 203, 204, 205, 206, 207, 208, 214, 226,
    300, 301, 302, 303, 304, 305, 307, 308,
    400, 401, 402, 403, 404, 405, 406, 407, 408, 409,
    410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421,
    422, 423, 424, 425, 426, 428, 429, 431,
    444, 450, 451, 495, 496, 497, 498, 499,
    500, 501, 502, 503, 504, 506, 507, 508, 509, 510, 511,
    521, 522, 523, 525, 530, 599
]

bot = Bot(token=TOKEN)

config = configparser.ConfigParser()

async def get_index():
    config.read("config.ini")
    index = config["index"]["index"] 
    return int(index)

async def increment_index():
    config.read("config.ini")
    index = int(config["index"]["index"]) 
    index += 1
    config["index"]["index"] = str(index)
    with open('config.ini', 'w') as configfile:
      config.write(configfile)

async def send_daily_content():
    index = await get_index()
    url = BASE_URL + str(http_error_codes[index])
    await bot.send_photo(
        chat_id=CHAT_ID, photo=url, caption="Here's your daily cat! 😺"
    )
    await increment_index()

if __name__ == "__main__":
    asyncio.run(send_daily_content())
