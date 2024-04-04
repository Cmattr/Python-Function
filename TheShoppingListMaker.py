shopping_list = []


def add_item (input, shopping_list):
    shopping_list.append(input)

def remove_item(input,shoppinlist):
    shopping_list.remove(input)


selection = ''

while selection != '4':
    print('''hello welcome to the shopping list
    please select an option by number below
    1. add an item to the shopping list
    2. remove an item from the shopping list
    3. view the shopping list
    4. exit''')
    selection = input("select an option by number: ")

    if selection == '1':
        add = str(input("what would you like to add to the shopping list? "))
        add_item(add, shopping_list)
        print((add) + "has been added to your shopping list" )
    elif selection == '2':
        remove = str(input("what would you like to remove from the shopping list? "))
        remove_item(remove, shopping_list)
        print((remove) + "has been added to your shopping list" )
    elif selection == '3':
         print(f'''\nthe shopping list includes:
     {shopping_list}\n''')
    else: 
        pass

        

   