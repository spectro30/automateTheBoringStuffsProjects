def displayInventory(inventory):
    item_total = 0
    print('Inventory :')
    for i in inventory.keys():
        print( str(inventory[i]) +' ' + i)
        item_total  += inventory[i]
    print('Total number of items: ' + str(item_total))

def addToInventory(inventory, addedItems):
    
    for i in addedItems :
        inventory[i] = inventory.get(i, 0) + 1
    return inventory


inv = {'gold coin' : 42, 'rope' : 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
