items = {
    "127392": {"name": "Banana", "price": 4},
    "1255477": {"name": "Chicken", "price": 12},
    "82991": {"name": "Milk", "price": 5},
    "86937": {"name": "Water", "price": 15},
    "746578": {"name": "Eggs", "price": 10}
}

money = 1000

barcode = input("Please enter your item's barcode number: ")

if barcode in items:
    item = items[barcode]
    if money >= item["price"]:
        money -= item["price"]
        print(f"Purchased {item['name']} for ${item['price']}. Remaining balance: ${money}")
    else:
        print("Not enough money!")
else:
    print("Item not found (invalid barcode).")
