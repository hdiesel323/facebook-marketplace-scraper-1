import requests
from bs4 import BeautifulSoup
import json
import time
from config import SCRAPING_BEE_API_KEY
from scraper_utils import extract_product_info, save_to_json

def validate_api_key(api_key):
    if not api_key or not isinstance(api_key, str) or len(api_key) < 32:
        raise ValueError("Invalid Scraping Bee API key. Please check your configuration.")

def ensure_scraping_bee_request(url, params):
    if not url.startswith("https://app.scrapingbee.com/api/v1/"):
        raise ValueError("Direct scraping from Facebook is not allowed. Use Scraping Bee API.")
    if 'api_key' not in params or params['api_key'] != SCRAPING_BEE_API_KEY:
        raise ValueError("Invalid or missing Scraping Bee API key in the request.")

def scrape_facebook_marketplace(search_query, num_pages=5, max_retries=3):
    print("Initializing scraper with Scraping Bee API...")
    validate_api_key(SCRAPING_BEE_API_KEY)
    print(f"Scraping Bee API key validated. Length: {len(SCRAPING_BEE_API_KEY)} characters")
    
    base_url = "https://www.facebook.com/marketplace/search/?query="
    api_url = "https://app.scrapingbee.com/api/v1/"

    params = {
        "api_key": SCRAPING_BEE_API_KEY,
        "url": base_url + search_query,
        "render_js": "false",
    }

    all_products = []

    print(f"Starting to scrape Facebook Marketplace for '{search_query}' using Scraping Bee...")

    for page in range(1, num_pages + 1):
        print(f"Scraping page {page}...")
        print(f"Sending request to Scraping Bee API for page {page}...")
        
        for attempt in range(max_retries):
            try:
                ensure_scraping_bee_request(api_url, params)
                response = requests.get(api_url, params=params)
                print(f"Received response from Scraping Bee. Status code: {response.status_code}")
                response.raise_for_status()
                
                soup = BeautifulSoup(response.text, 'html.parser')
                product_cards = soup.find_all('div', class_='x9f619 x78zum5 x1r8uery xdt5ytf x1iyjqo2 xs83m0k x1e558r4 x150jy0e x1iorvi4 xjkvuk6 x1a2a7pz')
                
                for card in product_cards:
                    product_info = extract_product_info(card)
                    if product_info:
                        all_products.append(product_info)
                
                # Handle pagination
                next_page = soup.find('a', {'aria-label': 'Next'})
                if next_page:
                    params['url'] = "https://www.facebook.com" + next_page['href']
                else:
                    print("No more pages to scrape.")
                    break
                
                break  # Success, break the retry loop
            
            except requests.RequestException as e:
                print(f"Error occurred: {e}")
                if attempt < max_retries - 1:
                    print(f"Retrying in 5 seconds... (Attempt {attempt + 2}/{max_retries})")
                    time.sleep(5)
                else:
                    print("Max retries reached. Moving to the next page.")
            except ValueError as e:
                print(f"Scraping error: {e}")
                return
        
        time.sleep(2)  # Add a delay between pages to avoid rate limiting

    # Save the scraped data to a JSON file
    save_to_json(all_products, "output/facebook_marketplace_products.json")
    print(f"Scraping complete. {len(all_products)} products saved to output/facebook_marketplace_products.json")

if __name__ == "__main__":
    try:
        validate_api_key(SCRAPING_BEE_API_KEY)
        search_query = input("Enter your search query for Facebook Marketplace: ")
        num_pages = int(input("Enter the number of pages to scrape (default is 5): ") or 5)
        scrape_facebook_marketplace(search_query, num_pages)
    except ValueError as e:
        print(f"Error: {e}")
        print("Please check your Scraping Bee API key in the config.py file.")
