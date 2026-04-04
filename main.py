from read import load_products
from operations import display_products, sell_product, restock_product
from write import save_products

def main():
    """
    Main function to handle the WeCare Store Manager application.
    Provides a menu for users to display, sell, and restock products.
    """
    try:
        # Load products from the file
        products = load_products()
    except Exception as e:
        print(f"Error loading products: {e}")
        return

    while True:
        # Display the menu
        print("\n--- WeCare Store Menu ---")
        print("1. Display Products")
        print("2. Sell Products")
        print("3. Restock Products")
        print("4. Exit")

      
