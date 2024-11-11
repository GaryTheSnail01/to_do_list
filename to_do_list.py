#Start with a main menu that lists options to...
    #Add tasks
    #View tasks
    #Delete tasks
    #Quit the application
#Tasks should be stored in a list
#Error handling w/ try, except, else, and finally

import sys

stored_tasks = []
err_msg = "An error has occured, please try again."
inv_msg = "Invalid input, please try again."
main_menu_msg = "Returning to the main menu..."

def start():
    print("Main Menu")
    print("Please choose from the following options:")
    
    menu_options = {
        1: ("Add Tasks", add_task),
        2: ("View Tasks", view_task),
        3: ("Delete Tasks", del_task),
        4: ("Quit", quit)
    }
    
    #print each option from the menu_options dic. w/ the corresponding # in front.
    for num, (option, func) in menu_options.items():
        print(f"{num} - {option}")
        
    try:
        answer = int(input(""))
        if answer in menu_options:
            menu_options[answer][1](stored_tasks)
        else:
            print(inv_msg)
            start()
            
    except (TypeError, ValueError) as e:
        print(err_msg)
        start()

def add_task(stored_tasks):
    print("Add a Task Menu")
    
    try:
        num_of_tasks = int(input("How many tasks would you like to add? "))
        while num_of_tasks > 0:
            name_of_task = input("Add your task: ")
            stored_tasks.append(name_of_task)
            print(f"{name_of_task} has been added to your to do list!")
            num_of_tasks -= 1
            
    except (TypeError, ValueError) as e:
        print(err_msg)
        add_task(stored_tasks)

    print(main_menu_msg)
    start()

def view_task(stored_tasks):
    if stored_tasks == []:
        print(f"Looks like you don't have any tasks saved yet! Enter the 'Add Tasks' menu to add a new task. \n{main_menu_msg}")
        start()
    else:
        try:
            print("Here are your tasks:")
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
    pass

def quit():
    print("Closing application...")
    sys.exit()
    
start()