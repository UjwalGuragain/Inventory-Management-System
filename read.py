PRODUCTS_FILE = 'products.txt'

def load_products():
    """
    Load product details from a file into a dictionary.

    Returns:
        dict: A dictionary containing product details.
    """
    products = {}
    try:
        with open(PRODUCTS_FILE, 'r') as file:
            for line in file:
                if line.strip():
                    # Analyze product details from the file
                    name, brand, quantity, cost_price, country = line.strip().split(',')
                    name_key = name.strip().lower()
                    products[name_key] = {
                        'name': name.strip(),
                        'brand': brand.strip(),
                        'quantity': int(quantity.strip()),
                        'cost_price': float(cost_price.strip()),
                        'country': country.strip()
                    }
    except FileNotFoundError:
        print("No existing product file found.")
    except Exception as e:
        print(f"Error loading products: {e}")

    if not products:
        print("Warning: No products loaded. The file may be empty or missing.")

    return products
