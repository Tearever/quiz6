class Customer:
    def __init__(self, customer_info):
        self.customer_info = customer_info

    def get_customer_info(self):
        return self.customer_info

class Item:
    def __init__(self, item_name, price):
        self.item_name = item_name
        self.price = price
    
    def get_item_name(self):
        return self.item_name

    def get_price(self):
        return self.price

class Cost_Calculator:
    def __init__(self, items, tax, discount):
        self.items = items
        self.tax = tax
        self.discount = discount

    def calculate_total_cost(self):
        total_cost = sum(item.get_price() for item in self.items)
        if(self.discount > 0):
            if(self.discount > 0 and self.discount < 1):
                total_cost = total_cost * self.discount
            else:
                self.discount = self.discount / 100
                total_cost = total_cost * self.discount
        tax_total = total_cost * self.tax
        return total_cost + tax_total

class Validate_order_data(self):
    is_valid = True
    print("Order data validation successful" if is_valid else "Order data validation failed")


def main():
    customer = Customer("Trevor Wright")
    item1 = Item(item_name="T-shirt", price=50.00)
    item2 = Item(item_name="DUNE book", price=35.00)
    item3 = Item(item_name="Helldivers 2", price=39.99)

    items = [item1, item2, item3]

    order_calulator = Cost_Calculator(items, 0.10, 0)

    print(order_calulator.calculate_total_cost())


if __name__ == "__main__":
    main()

    