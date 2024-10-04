import os

# Scraping Bee API Key
SCRAPING_BEE_API_KEY = os.environ.get('SCRAPING_BEE_API_KEY')

# IMPORTANT: The API key is now being loaded from the environment variable.
# If you need to set it manually, replace the line above with your actual Scraping Bee API key.
# Example: SCRAPING_BEE_API_KEY = "your_actual_api_key_here"

# If you don't have a Scraping Bee API key, sign up at https://www.scrapingbee.com/
# and set the environment variable SCRAPING_BEE_API_KEY with your actual API key.
# Failing to set a valid API key will result in the script not functioning properly.
