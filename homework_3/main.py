class ItemToPurchase:

    def __init__(self, name='none', price=0, quantity=0, description='none'):
        self.item_name = name
        self.item_description = description
        self.item_price = price
        self.item_quantity = quantity

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print('%s %d @ $%d = $%d' % (self.item_name, self.item_quantity, self.item_price, total))


first_item = ItemToPurchase()

second_item = ItemToPurchase()



print("Item 1")
first_item.item_name = input(str("Enter the item name:\n"))
first_item.item_price = int(input("Enter the item price:\n"))
first_item.item_quantity = int(input("Enter the item quantity:\n"))
print()

print("Item 2")
second_item.item_name = input(str("Enter the item name:\n"))
second_item.item_price = int(input("Enter the item price:\n"))
second_item.item_quantity = int(input("Enter the item quantity:\n"))


print("\nTOTAL COST")
first_item.print_item_cost()
second_item.print_item_cost()
print()

Total = first_item.item_price*first_item.item_quantity+second_item.item_price*second_item.item_quantity

print("Total: $"+str(Total))
