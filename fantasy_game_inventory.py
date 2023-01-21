# Fantasy Game Inventory : Project Chapter 5
inventory_stuff = {'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6, 'dagger': 1}

def displayInventory(stuff):
    '''
    To display the inventory items.
    '''
    print('Inventory:')
    item_total = 0
    for k, v in stuff.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items: ' + str(item_total))

displayInventory(inventory_stuff)

def addToInventory(inventory, addedItems):

    '''
    to add the looted items(list) in the dictionary
    '''

    for i in addedItems:
        inventory.setdefault(i, 0)
        inventory[i] += 1
    displayInventory(inventory_stuff)
    return inventory


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'platinum']

# def addToDict(inventory, lst): # The best solution "Sometimes the solution is easy but make it complex"
#     for i in lst:
#         inventory.setdefault(i, 0)
#         inventory[i] += 1
#     return inventory
        

print(addToInventory(inventory_stuff, dragonLoot))