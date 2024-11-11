#Start with a main menu that lists options to...
    #Add tasks
    #View tasks
    #Delete tasks
    #Quit the application
#Tasks should be stored in a list
#Error handling w/ try, except, else, and finally
    #I know that finally prints out something reguardless if the code worked or not, but I didn't see a need for it in this program.

import sys

stored_tasks = []
err_msg = "An error has occured, please try again.\n"
inv_msg = "Invalid input, please try again.\n"
main_menu_msg = "Returning to the main menu...\n"

def start():
    print("Main Menu")
    print("Please choose from the following options:")
    
    #attaching the functions w/ what's printed in the main menu within a dictionary.
    menu_options = {
        1: ("Add Tasks", add_task),
        2: ("View Tasks", view_task),
        3: ("Delete Tasks", del_task),
        0: ("Quit", quit)
    }
    
    #print each option from the menu_options dic. w/ the corresponding # in front.
    for num, (option, func) in menu_options.items():
        print(f"{num} - {option}")
        
    try:
        answer = int(input(""))
        #since we don't want to pass stored_tasks as an arugment to quit, since quit doesn't take an arugment, 
        #it has been separated from the two lines of code below.
        if answer == 0:
            quit()
        #call the function that the user entered w/ stored_tasks as an argument so that the functions can edit the list.
        elif answer in menu_options:
            menu_options[answer][1](stored_tasks)
        else:
            print(inv_msg)
            start()
            
    except (TypeError, ValueError) as e:
        print(err_msg)
        start()

def add_task(stored_tasks):
    print("\nAdd a Task Menu\n")
    
    try:
        num_of_tasks = int(input("How many tasks would you like to add? Enter '0' to return to the main menu. "))
        while num_of_tasks > 0:
            name_of_task = input("Add your task: ")
            #check to see if user entered anything, can't enter an empty string
            if name_of_task:
                stored_tasks.append(name_of_task)
                print(f"{name_of_task} has been added to your to do list!\n")
                num_of_tasks -= 1
            else:
                print("Please name your task.")
                continue #skip to continue the loop
            
    except (TypeError, ValueError) as e:
        print(err_msg)
        add_task(stored_tasks)

    print(main_menu_msg)
    start()

def view_task(stored_tasks):
    if stored_tasks == []:
        print(f"Looks like you don't have any tasks saved yet! Enter the 'Add Tasks' menu to add a new task. \n{main_menu_msg}\n")
        start()
    else:
        try:
            print("\nViewing Saved Tasks\n")
            for task in stored_tasks:
                print(task)
                
            back_to_main = input("\nEnter '0' to return to the main menu. ")
            if back_to_main == '0':
                print(main_menu_msg)
                start()
            else:
                print(inv_msg)
                view_task(stored_tasks)
                
        except (TypeError, ValueError) as e:
            print(err_msg)
            view_task(stored_tasks)

def del_task(stored_tasks):
    if stored_tasks == []:
        print(f"Looks like you don't have any tasks saved yet! Enter the 'Add Tasks' menu to add a new task. \n{main_menu_msg}\n")
        start()
    else:
        try:
            print("\nDelete a Task\nHere are your saved tasks\n")
            for task in stored_tasks:
                print(task)
                
            print("\nThis is case sensitive, please be sure to enter your task exactly as shown.\nEnter '0' to return to the main menu.")
            selected_task = input("\nWhat task would you like to remove? ")
            if selected_task == '0':
                print(main_menu_msg)
                start()
            #if the entered task is inside of our list we remove it from our list.
            elif selected_task in stored_tasks:
                stored_tasks.remove(selected_task)
                print(f"{selected_task} has been removed from your to do list!\n")
                print(main_menu_msg)
                start()
            else:
                print(f"{inv_msg} Please enter a saved task.")
                del_task(stored_tasks)
                
        except (TypeError, ValueError) as e:
            print(err_msg)
            del_task(stored_tasks)

def quit():
        print("Closing application...")
        sys.exit()
        
#essentially starting the program
start()