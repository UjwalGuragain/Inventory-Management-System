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

  choice = input("Enter your choice: ")

        try:
            if choice == '1':
                # Display all products
                display_products(products)
            elif choice == '2':
                # Handle selling products
                sell_product(products)
            elif choice == '3':
                # Handle restocking products
                restock_product(products)
            elif choice == '4':
                # Exit the application
                print("Thank you for using WeCare Store Manager!")
                break
            else:
                print("Invalid choice. Please try again!")
        except Exception as e:
            print(f"An error occurred: {e}")
        else:
            # Save changes after successful operations
            save_products(products)

if __name__ == '__main__':
    main()      
