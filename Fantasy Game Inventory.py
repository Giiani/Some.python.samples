def displayInventory(items):
    total=0
    print("Inventory:")
    for name,quantity in items.items():
        total += quantity
        print(str(quantity)+" "+name)
    
    print("Total number of items:"+str(total))
    
items={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

displayInventory(items)