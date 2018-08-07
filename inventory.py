stuff = {'rope' : 1, 'torch' : 6, 'golden coin' : 42, 'dagger' : 1, 'arrow' : 12}

def displayInventory(inventory):
    item_total = 0
    print('Inventory :')
    for i in inventory.keys():
        print( str(inventory[i]) +' ' + i)
        item_total  += inventory[i]
    print('Total number of items: ' + str(item_total))

displayInventory(stuff)



