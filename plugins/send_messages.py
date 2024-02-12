import os
import time

from pyrogram import Client, filters, enums
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

load_dotenv()
users = {}
_api_id = os.getenv('API_ID')
_api_hash = os.getenv('API_HASH')
_bot_token = os.getenv('BOT_TOKEN')
_app = Client("acdc_bot", _api_id, _api_hash, bot_token=_bot_token)


def dynamic_data_filter(data: str):
    """
    Filter for dynamic data
    :param data: the data to search
    :return: the filter
    """

    async def func(flt, _, query):
        return flt.data == query.data

    return filters.create(func, data=data)


@_app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("Hello! I'm AC⚡️DC bot.\nI will send you a message when AC/DC announces a new tour. "
                       "You can check my source code [here](https://github.com/jimpo26/acdc-tour-notifier).\n"
                       "Remember to leave a ⭐️!\nThis bot was made by @jimpo26.")
    users[message.from_user.id] = (False, "")


@_app.on_callback_query(dynamic_data_filter("unsubscribe"))
def unsubscribe(client, query):
    """
    Unsubscribe the user
    :param client: the client
    :param query: the query
    """
    users[query.from_user.id] = (None, "")
    query.answer("You have been correctly unsubscribed")


def send_messages_to_users(tours):
    """
    Send a message to all the users
    :param tours: the tours
    """
    for user_id in users:
        print(user_id)
        if (users[user_id][0] and users[user_id][1] == tours) or users[user_id][0] is None:
            continue
        print("Sending message")
        message = "New tour announced!\n\n"
        for tour in tours:
            message += f"🎸 **{tour['date']}** 🎸\n" \
                       f"**Location**: {tour['location']}\n" \
                       f"**Venue**: {tour['venue']}\n" \
                       f"**Purchase link**: [🎟️Buy here]({tour['purchase_link']})\n\n"

        message += ("I will send a notification when something changes. If you don't want to receive other "
                    "notifications click the button below.")
        count = 0
        while count < 5:
            try:
                _app.send_message(chat_id=user_id,
                                  text=message,
                                  reply_markup=InlineKeyboardMarkup(
                                      [[InlineKeyboardButton("Unsubscribe", callback_data="unsubscribe")]]),
                                  parse_mode=enums.ParseMode.MARKDOWN)
                break
            except FloodWait as e:
                count += 1
                time.sleep(e.value)
            except Exception as e:
                break
        users[user_id] = (True, tours)


def start_bot():
    _app.run()
