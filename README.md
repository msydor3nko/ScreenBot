# ScreenBot
The simple Telegram Bot taking webpage screenshot with Python Selenium and Chrome Webdriver.

## How to prepare ScreenBot for running

**You need:** Git, Python3 (pytelegrambotapi, selenium), Pipenv, Chrome Browser, Chrome Webdriver
> Current bot using ChromeDriver 83.0.4103.39 for mac64

### Follow by steps

* Clone the App repository using Git

`git clone https://github.com/msydor3nko/ScreenBot.git`

* Enter to the 'ScreenBot' directory

`cd ScreenBot`

* Activate virtual environment

`pipenv shell`

* Install all needed libraries from 'Pipfile'

`pipenv install`

* Create '_config.py' file into 'ScreenBot' directory and put there Telegram Bot token:

`TOKEN = '<token_string>'`

* Following by the link bellow to Download Chrome Webdriver apropriate to your platform and Chrome Browser version:

`https://chromedriver.chromium.org/downloads`

* Put downloaded Chrome Webdriver into 'ScreenBot' directory and named it 'chromedriver'

## How to run the ScreenBot

* Run 'bot.py' file

`python bot.py`

* Find ScreenBot in Telegram by name '@AlphaBots_screenBot' and starting interaction

* Send URL to Telegram Bot for getting screenshot of the webpage (or look at the 'static' dir)
