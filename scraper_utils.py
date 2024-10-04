import json

def extract_product_info(card):
    try:
        title = card.find('span', class_='x1lliihq x6ikm8r x10wlt62 x1n2onr6').text.strip()
        price = card.find('span', class_='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x676frb x1lkfr7t x1lbecb7 x1s688f xzsf02u').text.strip()
        location = card.find('span', class_='x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft').text.strip()
        
        return {
            'title': title,
            'price': price,
            'location': location
        }
    except AttributeError:
        print("Failed to extract product information. The page structure might have changed.")
        return None

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

