# Best Buy Bot

## Features
- Refreshes link until "Add to Cart" button is available
- Automate entire checkout process

## Prerequisites
- Sign up for a Best Buy account
- Add all billing/shipping info to your account (must only have one card on the account)

## Dependencies
- Selenium
	- `pip install selenium`
- [Google Chrome](https://www.google.com/chrome/)
- [ChromeDriver](https://chromedriver.chromium.org/downloads)
	- Extract the compressed chromedriver executable to a driectory of your choice (be sure to update the path in bot.py accordingly)
		- For the Windows machine I developed this on, I chose `C:\Program Files (x86)\ChromeDriver\chromedriver.exe`

## Running the Bot
1. Make sure you have [Python 3.9](https://www.python.org/downloads/release/python-390/)
2. Edit the info.py file with your Best Buy account email and password and cvv for the card on the account
3. Navigate to your project directory and run the bot.py script from your preferred environment
4. Ensure that your Best Buy account has a main shipping address saved and a main Credit Card saved, otherwise the click logic won't work.
5. Feel free to change the Best Buy links in the bot.py file to any item on bestbuy.com

