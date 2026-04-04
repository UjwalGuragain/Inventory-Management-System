from write import generate_sale_invoice, generate_restock_invoice, save_products

def display_products(products):
    """
    Display all available products in a tabular format using string formatting.

    Args:
        products (dict): A dictionary containing product details.
    """
    if not products:
        print("\nNo products available to display.")
        return

    # Print table header
    print("\nAvailable Products:")
    print("=" * 70)
    print(f"{'Product':<18} {'Brand':<12} {'Stock':<8} {'Selling Price (Rs.)':<20} {'Country':<10}")
    print("-" * 70)

    # Print each product in the table
    for details in products.values():
        # Selling price is calculated as double the cost price
        selling_price = details['cost_price'] * 2
        print(f"{details['name']:<18} {details['brand']:<12} {details['quantity']:<8} Rs.{selling_price:<18.2f} {details['country']:<10}")

    print("=" * 70)

def sell_product(products):
    """
    Handle the process of selling products to a customer.

    Args:
        products (dict): A dictionary containing product details.
    """
    customer_name = input("Enter customer's name: ")
    cart = []  # List to store purchased items
    total_amount = 0  # Total amount for the purchase

    while True:
        product_name = input("Enter product name to buy (or 'done' to finish): ")
        if product_name.lower() == 'done':
            break

        key = product_name.lower()
        if key not in products:
            print("Product not found!")
            continue

        try:
            quantity = int(input("Enter quantity to buy: "))
            if quantity <= 0:
                raise ValueError
        except ValueError:
            print("Invalid quantity! Please enter a positive integer.")
            continue

        available_quantity = products[key]['quantity']
        free_items = quantity // 3  # Calculate free items (1 free for every 3 purchased)
        total_items = quantity + free_items

        if total_items > available_quantity:
            print(f"Not enough stock. Only {available_quantity} items available including free ones.")
            continue

        print(f"You will receive {free_items} free items with your purchase.")

        # Calculate the selling price and total amount for the product
        selling_price = products[key]['cost_price'] * 2
        amount = selling_price * quantity
        total_amount += amount
        products[key]['quantity'] -= total_items  # Deduct purchased and free items from stock

        # Add the product to the cart
        cart.append((products[key], quantity, amount))

    if cart:
        # Generate and display the sales invoice
        generate_sale_invoice(cart, customer_name)
    else:
        print("No items purchased.")

def restock_product(products):
    """
    Handle the process of restocking products from a supplier.

    Args:
        products (dict): A dictionary containing product details.
    """
    supplier_name = input("Enter supplier's name: ")
    restock_list = []  # List to store restocked items
    total_cost = 0  # Total cost for the restocked items

    while True:
        product_name = input("Enter product name to restock (or 'done' to finish): ")
        if product_name.lower() == 'done':
            break

        key = product_name.lower()
        try:
            quantity = int(input("Enter quantity to add: "))
            if quantity <= 0:
                raise ValueError
            new_cost_price = float(input("Enter new cost price: "))
            if new_cost_price <= 0:
                raise ValueError
        except ValueError:
            print("Invalid quantity or price! Please enter positive numbers.")
            continue

        if key in products:
            # Update existing product details
            products[key]['quantity'] += quantity
            products[key]['cost_price'] = new_cost_price
        else:
            # Add a new product to the inventory
            brand = input("Enter brand: ").strip()
            if not brand:
                print("Brand cannot be empty.")
                continue

            country = input("Enter country of origin: ").strip()
            if not country:
                print("Country cannot be empty.")
                continue

            products[key] = {
                'name': product_name.strip(),
                'brand': brand,
                'quantity': quantity,
                'cost_price': new_cost_price,
                'country': country
            }

        # Calculate the cost for the restocked quantity
        cost = quantity * new_cost_price
        total_cost += cost
        restock_list.append((products[key], quantity))

    if restock_list:
        # Generate and display the restock invoice
        generate_restock_invoice(restock_list, supplier_name)

    # Save the updated product details to the file
    save_products(products)
