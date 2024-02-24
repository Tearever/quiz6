class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class OrderDetails:
    def __init__(self, customer, items, shipping_address):
        self.customer = customer
        self.items = items
        self.shipping_address = shipping_address

class CostCalculator:
    def calculate_total_cost(order_details):
        total_cost = 0
        print("Calculating total order cost...")
        return total_cost

class OrderValidator:
    def validate_order(order_details):
        print("Validating order data...")

class EmailSender:
    def send_order_confirmation_email(customer_email):
        print(f"Sending order confirmation email to {customer_email}...")

class InventoryUpdater:
    def update_inventory(order_details):
        print("Updating inventory levels...")

def main():
    customer = Customer("John Doe", "john@example.com", "123 Main St")
    item1 = Item("Item1", 20.0, 2)
    item2 = Item("Item2", 30.0, 1)
    items = [item1, item2]
    shipping_address = "456 Side St"

    order_details = OrderDetails(customer, items, shipping_address)

    CostCalculator.calculate_total_cost(order_details)
    OrderValidator.validate_order(order_details)
    EmailSender.send_order_confirmation_email(customer.email)
    InventoryUpdater.update_inventory(order_details)

if __name__ == "__main__":
    main()
