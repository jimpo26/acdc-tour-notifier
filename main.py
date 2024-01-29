from dotenv import load_dotenv
from threading import Thread

from get_tour_info import start
from plugins.send_messages import start_bot

if __name__ == '__main__':
    load_dotenv()
    Thread(target=start).start()
    start_bot()
