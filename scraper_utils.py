import json
import logging

def extract_product_info(card):
    try:
        title_element = card.find('span', class_='x1lliihq x6ikm8r x10wlt62 x1n2onr6')
        price_element = card.find('span', class_='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x676frb x1lkfr7t x1lbecb7 x1s688f xzsf02u')
        location_element = card.find('span', class_='x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft')
        
        if not all([title_element, price_element, location_element]):
            logging.warning("Some elements not found. Trying alternative selectors.")
            title_element = card.find('span', class_='x1lliihq x6ikm8r x10wlt62 x1n2onr6')
            price_element = card.find('span', class_='x193iq5w')
            location_element = card.find('span', class_='x1lliihq')

        title = title_element.text.strip() if title_element else "N/A"
        price = price_element.text.strip() if price_element else "N/A"
        location = location_element.text.strip() if location_element else "N/A"
        
        image_element = card.find('img')
        image_url = image_element['src'] if image_element and 'src' in image_element.attrs else "N/A"
        
        product_url_element = card.find('a', href=True)
        product_url = "https://www.facebook.com" + product_url_element['href'] if product_url_element else "N/A"

        return {
            'title': title,
            'price': price,
            'location': location,
            'image_url': image_url,
            'product_url': product_url
        }
    except Exception as e:
        logging.error(f"Failed to extract product information: {e}")
        logging.debug(f"Card HTML: {card}")
        return None

def save_to_json(data, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        logging.info(f"Data successfully saved to {filename}")
    except Exception as e:
        logging.error(f"Failed to save data to JSON: {e}")

