 Facebook Marketplace Scraper
This project scrapes product data from Facebook Marketplace using Scraping Bee's API and BeautifulSoup. The extracted data is saved in a JSON file.
## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Configuration](#configuration)
4. [Logging](#logging)
5. [Contributing](#contributing)
6. [License](#license)
7. [Contact](#contact)
## Installation
To install this project, follow these steps:
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/facebook-marketplace-scraper.git
    cd facebook-marketplace-scraper
    ```
2. Install the required dependencies using [Poetry](pyproject.toml):
    ```bash
    poetry install
    ```
## Usage
To run the scraper, execute the following command and follow the prompts to input your search query and the number of pages to scrape:
```bash
poetry run python fb_marketplace_scraper.py
The results will be saved in output/facebook_marketplace_products.json.

Configuration
You must set the Scraping Bee API key in your environment variables. The key is fetched using:

SCRAPING_BEE_API_KEY = os.environ.get('SCRAPING_BEE_API_KEY')
Make sure to set your environment variable correctly:

export SCRAPING_BEE_API_KEY=your_api_key_here
Logging
The application logs are set to provide information on the scraping process, including API validation and number of products extracted. Logs are displayed in the console, showing each step of the process.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any proposed changes.

License
This project is licensed under the MIT License. See the LICENSE file for more information.

Contact
For questions, please reach out to:

Email: your-email@example.com
GitHub: yourusername