menu = {
    "coffee": 2.5,
    "tea": 2.0,
    "pastry": 1.5,
    "water": 1.0,
    "juice": 2.0
}

print('\n <---Welcome to the Cafe! Here is our menu:---> \n ')
print('Menu: \n')

for item, price in menu.items():
    print(f"{item.title()}: ${price}")

order = {}

while True:
    item = input("enter your order :- ").lower()

    if item in menu:
        qty = int(input("enter the quantity :- "))
        order[item] = order.get(item, 0) + qty  # Fix: add qty to order
        print(f"Your order {qty} {item} is added successfully")
    else:
        print("Sorry, we don't have that item. Please choose from the menu.")

    any_order = input("Do you want to order anything else? (yes) or (no): ").lower()
    if any_order == "no":
        break

# Bill and thank you message after ordering is done
print("\n-------------------------------")
total_amt = 0
for item, qty in order.items():
    price = menu[item] * qty
    total_amt += price
    print(f"{item.title()} x {qty} = ${price:.2f}")

print("-------------------------------")
print(f"Total amount: ${total_amt:.2f}")
print("Thank you for visiting the Cafe! Have a great day!")