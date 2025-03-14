# idea: pretty print the list (1 item on each line)
# idea: clear the screen after we print the list
# idea: delete item from the list
# idea: edit an item in the list
# idea: add numbers to the items when I print them out
# idea: print in color (q: does it need a special library?)

import os # import the 'os' library

# clear the terminal window before everything else
os.system('cls' if os.name == 'nt' else 'clear')
print("Welcome to my to-do list app!") # greet the user
my_list = [] # make a list to save items
while True:
    # save the newly inputted item
    new_item = input("Please enter a new item or 'q' to quit: ")
    if new_item == 'q':
        print("Goodbye!")
        break
    else:
        my_list.append(new_item) # add new item to list
        os.system('cls' if os.name == 'nt' else 'clear')
        for item in my_list:
            print(item)
