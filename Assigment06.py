# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# Chris Messmann, 11/21/2020,Pasted relevant Assignment05 code into their appropriate class/functions
# Chris Messmann, 11/22/2020,Added option for user to specify which record to delete
# Chris Messmann, 11/23/2020,Modified code to process I/O return values in Processing
# Chris Messmann, 11/24/2020,Cleaned up and commented code to complete assignment 6
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
objFile = None   # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions

# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        dicRow = {"Task": task.strip(), "Priority": priority.strip()}
        list_of_rows.append(dicRow)
        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(taskNum, list_of_rows):
        # Capture row number to delete

        list_of_rows.remove(list_of_rows[taskNum])  # Remove row
        print(f'\nTask {taskNum} has been removed.')

        return list_of_rows, 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        objFile = open(file_name, "w")
        for row in list_of_rows:
            objFile.write(row["Task"].lower() + "," + row["Priority"].lower() + "\n")
        objFile.close()
        print("Your data has been saved to the file 'ToDoList.txt'")
        return list_of_rows, 'Success'

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        print("Enter a new Task and Priority")
        task = input("Task: ").lower()
        priority = input("Priority: ").lower()
        return task, priority

    @staticmethod
    def input_task_to_remove(list_of_rows):

        """The remove row functions are a departure from my previous homework.  Previously
        the user was only able to delete their last data entry.  In this assignment I would like
        to provide the user with the option of selecting which item from the list to delete.
        There's probably of number of ways of doing this but I think the mose intuitive is to
         order to do that I assign a row number (via variable and counter) to each row
         in the list.  This was best accomplished by a classmate in assignment 5.  Ref their github
         page:  https://github.com/rayeni/IntroToProg-Python/blob/main/Assignment05.py > Lines 84-96
         for the source"""

        # Capture row number to delete and send it to 'remove_data_from_list' function

        i = 0  # local variable to act as counter to number rows
        print("Task No.| Task (Priority)")  # Data header
        for row in list_of_rows:  # loop through list of dictionaries
            print(f'{i} \t| {row["Task"]} ({row["Priority"]})')
            i += 1
        print()  # print new line
        taskNum = int(input("Enter the Task No. you would like to remove:  "))
        return taskNum

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while(True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option
    
    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        strTask, strPriority = IO.input_new_task_and_priority()             #Setting strTask and strPriority = return values 'task' and 'priority' from input_new_task_and_priority
        Processor.add_data_to_list(strTask, strPriority, lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        strTask = IO.input_task_to_remove(lstTable)
        Processor.remove_data_from_list(strTask, lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':   # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            Processor.write_data_to_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            Processor.read_data_from_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  #  Exit Program
        print("Goodbye!")
        input("Enter to Exit", )
        break   # and Exit
