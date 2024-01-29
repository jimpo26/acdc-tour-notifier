# AC⚡️DC Tour notifications
This bot will send you a telegram notification when AC⚡️DC announces a new tour date.
You can find it on telegram as [@acdcTourNotifier_bot](https://t.me/acdcTourNotifier_bot).

## How this bot works
This bot uses web scraping to get data from [AC⚡️DC's official website](https://www.acdc.com/tour), and performs
a request every 2 minutes, so technically you will get a notification in less than 2 minutes after the announcement (if i don't get banned).
I haven't implemented any kind of protection against anti-bot systems yet. 

## Want to run locally?
If you want to run this bot locally, first you have to clone this repo using the command
`git clone github.com/jimpo26/acdc-tour-notifier.git`
Then, you have to create a .env file in the root of the project, and insert the following variables
```
BOT_TOKEN=
API_ID=
API_HASH=
```
Since this bot works with the MTProto api (and not the simple BotApi) you will need not only a bot token (that you can retrieve 
from [@BotFather](https://t.me/BotFather)), but also an api id and an api hash (you can get them from [my.telegram.org](https://my.telegram.org/)).

After that, you can create the virtualenvironment using the command `python3 -m venv venv`, and then activate it with `source venv/bin/activate`.
Then, you can start the bot with `python3 main.py`.

## Contributing
If you want to contribute to this project, you can open a pull request or an issue.

## Disclaimer
This project is not affiliated, associated, authorized, endorsed by, or in any way officially connected with AC⚡️DC, or any of its subsidiaries or its affiliates. The official AC⚡️DC website can be found at https://www.acdc.com/.
Note that this project comes without ANY warranty, so there is no guarantee that it will work as expected.
