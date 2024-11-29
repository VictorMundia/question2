import requests

API_URL = 'http://localhost:5000'

def add_product(name, description, price):
    response = requests.post(
        f'{API_URL}/products',
        json={
            'name': name,
            'description': description,
            'price': price
        }
    )
    print(f'Status Code: {response.status_code}')
    print('Response:', response.json())

def get_all_products():
    response = requests.get(f'{API_URL}/products')
    print('All Products:')
    for product in response.json():
        print(f"- {product['name']}: ${product['price']} - {product['description']}")

def main():
    # Add some sample products
    print("Adding new products...")
    add_product('Laptop', 'High-performance laptop', 999.99)
    add_product('Smartphone', 'Latest model smartphone', 699.99)
    
    # Try adding invalid product (should fail)
    print("\nTrying to add invalid product...")
    add_product('Invalid', 'Test product', -100)
    
    # Get all products
    print("\nRetrieving all products...")
    get_all_products()

if __name__ == '__main__':
    main()