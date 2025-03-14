# DONE: pretty print the list (1 item on each line)
# DONE: clear the screen before we print the list
# DONE: add dashes before each item
# DONE: add a title "My List" before the list is printed out
# idea: delete item from the list
# idea: edit an item in the list
# idea: add numbers to the items when I print them out
# idea: print in color (q: does it need a special library?)
# idea: not allow the user to enter empty "" (no text) items
import os # import the 'os' library

def my_clear_func():
    os.system('cls' if os.name == 'nt' else 'clear')

# clear the terminal window before everything else
my_clear_func()

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
        my_clear_func()
        print("My List:")
        for item in my_list:
            print("- " + item)