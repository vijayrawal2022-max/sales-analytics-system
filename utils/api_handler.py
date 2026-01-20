import requests

API_URL = "https://dummyjson.com/products?limit=100"


def fetch_all_products():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        print("✓ API fetch successful")
        return response.json().get('products', [])
    except:
        print("❌ API fetch failed")
        return []


def create_product_mapping(api_products):
    mapping = {}

    for product in api_products:
        mapping[product['id']] = {
            'category': product['category'],
            'brand': product['brand'],
            'rating': product['rating']
        }

    return mapping
