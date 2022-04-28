def displayInventory(items):
    total=0
    print("Inventory:")
    for name,quantity in items.items():
        total += quantity
        print(str(quantity)+" "+name)
    
    print("Total number of items:"+str(total))
    
def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        if addedItems[i] in inventory:
            inventory[addedItems[i]]+=1
        else:
            inventory.setdefault(addedItems[i],1)
    
    return inventory
            
            
items = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
addedItems = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
displayInventory(items)
items = addToInventory(items,addedItems)
displayInventory(items)