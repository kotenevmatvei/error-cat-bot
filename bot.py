import asyncio
from telegram import Bot

TOKEN = "7799366445:AAHDIFlFp1IF6hpovq05IPg5aRL0CnXkdKU"
CHAT_ID = 405557299
BASE_URL = "https://http.cat/"

global index 
index = 101

bot = Bot(token=TOKEN)


async def send_daily_content():
    global index
    url = BASE_URL + str(index)
    await bot.send_photo(
        chat_id=CHAT_ID, photo=url, caption="Here's your daily cat! 😺"
    )
    index += 1



if __name__ == "__main__":
    asyncio.run(send_daily_content())
