from datetime import datetime

PRODUCTS_FILE = 'products.txt'

def save_products(products):
    """
    Save product details to a file.

    Args:
        products (dict): A dictionary of product details.
    """
    try:
        with open(PRODUCTS_FILE, 'w') as file:
            for details in products.values():
                file.write(f"{details['name']}, {details['brand']}, {details['quantity']}, {details['cost_price']}, {details['country']}\n")
    except Exception as e:
        print(f"Error saving products: {e}")
        print("Please check file permissions or disk space and try again.")

def generate_restock_invoice(restock_items, supplier_name):
    """
    Generate and display a restock invoice with VAT included, and save it to a file.

    Args:
        restock_items (list): A list of tuples containing product details and quantities.
        supplier_name (str): The name of the supplier.
    """
    now = datetime.now()
    timestamp = f"{now.year}{now.month:02}{now.day:02}_{now.hour:02}{now.minute:02}{now.second:02}"
    filename = f"restock_invoice_{timestamp}.txt"
    total_amount = 0

    # Restock Invoice content
    invoice = []
    invoice.append("=" * 70)
    invoice.append(" - - - - - - - - - -WeCare Restock Invoice - - - - - - - - - - - - - -")
    invoice.append("=" * 70)
    invoice.append(f"Supplier Name : {supplier_name:<50}")
    invoice.append(f"Date          : {now.year}-{now.month:02}-{now.day:02}\t{now.hour:02}:{now.minute:02}:{now.second:02}")
    invoice.append("-" * 70)
    invoice.append(f"{'Product':<18}{'Brand':<12}{'Quantity':<10}{'Unit Price':<18}{'Total':<10}")
    invoice.append("-" * 70)

    for product, qty in restock_items:
        cost = qty * product['cost_price']
        total_amount += cost
        invoice.append(f"{product['name']:<18}{product['brand']:<12}{qty:<10}Rs.{product['cost_price']:<15.2f}Rs.{cost:<10.2f}")

    vat = total_amount * 0.13
    total_with_vat = total_amount + vat
    invoice.append("-" * 70)
    invoice.append(f"{'Subtotal':<58}Rs.{total_amount:<10.2f}")
    invoice.append(f"{'VAT (13%)':<58}Rs.{vat:<10.2f}")
    invoice.append(f"{'Total Restock Cost':<58}Rs.{total_with_vat:<10.2f}")
    invoice.append("=" * 70)
    invoice.append("Thank you for partnering with us!")
    invoice.append("=" * 70)

    # Write to file
    with open(filename, 'w') as file:
        file.write("\n".join(invoice))

    # Print to console
    print("\n".join(invoice))
    print(f"Restock invoice generated: {filename}")


def generate_sale_invoice(sale_items, buyer_name):
    """
    Generate and display a sales invoice with VAT included, and save it to a file.

    Args:
        sale_items (list): A list of tuples containing product details, quantities, and costs.
        buyer_name (str): The name of the buyer.
    """
    now = datetime.now()
    timestamp = f"{now.year}{now.month:02}{now.day:02}_{now.hour:02}{now.minute:02}{now.second:02}"
    filename = f"sale_invoice_{timestamp}.txt"
    total_amount = 0

    # Sale Invoice content
    invoice = []
    invoice.append("=" * 80)
    invoice.append(" - - - - - - - - - -WeCare Sales Invoice - - - - - - - - - - - - - - -")
    invoice.append("=" * 80)
    invoice.append(f"Buyer Name    : {buyer_name:<50}")
    invoice.append(f"Date          : {now.year}-{now.month:02}-{now.day:02}\t{now.hour:02}:{now.minute:02}:{now.second:02}")
    invoice.append("-" * 80)
    invoice.append(f"{'Product':<18}{'Brand':<12}{'Quantity':<10}{'Free Items':<12}{'Unit Price':<15}{'Total':<10}")
    invoice.append("-" * 80)

    total_items = 0
    total_discounts = 0

    for product, quantity, cost in sale_items:
        free_items = quantity // 3
        total_items += quantity + free_items
        total_discounts += free_items
        unit_price = product['cost_price'] * 2  # Calculate unit price as double the cost price
        total_amount += cost
        invoice.append(f"{product['name']:<18}{product['brand']:<12}{quantity:<10}{free_items:<12}Rs.{unit_price:<13.2f}Rs.{cost:<10.2f}")

    vat = total_amount * 0.13
    total_with_vat = total_amount + vat
    invoice.append("-" * 80)
    invoice.append(f"{'Subtotal':<68}Rs.{total_amount:<10.2f}")
    invoice.append(f"{'VAT (13%)':<68}Rs.{vat:<10.2f}")
    invoice.append(f"{'Total Amount':<68}Rs.{total_with_vat:<10.2f}")
    invoice.append("=" * 80)
    invoice.append("Thank you for shopping with us!")
    invoice.append("=" * 80)

    # Write to file
    with open(filename, 'w') as file:
        file.write("\n".join(invoice))

    # Print to console
    print("\n".join(invoice))
    print(f"Sale invoice generated: {filename}")
