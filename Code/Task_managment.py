from datetime import datetime
from time import sleep
import os 
import sys

#class Task that is used to create a Task
class Task:
    def __init__(self,name,description,due_date) -> None:
        self.name = name
        self.description = description
        self.due_date = due_date
        self.completed = False
    
    def complete_the_task(self):
        self.completed = True
    
    def __str__(self) -> str:
        return f"Task Name: {self.name}\nDescription: {self.description}\nDue_Date: {self.due_date}"

#class Task Managment -> to organize the task and make the appear to the user and complete the one that he done
class Task_Managment:
    def __init__(self) -> None:
        self.tasks = []
    
    #add the tasks to a list so that the list is displayed later 
    def add_task(self,task):
        self.tasks.append(task)
    
    #displays the tasks that the user created
    def view_tasks(self):
        
        #if the user hadn't put tasks yet it will return him the below message
        if not self.tasks:
            return "There are not Tasks at this moment"
        
        #else the program will output the tasks that he had putted
        else:
            for idx , ta_sk in enumerate(self.tasks,1):
              print(f"{idx}.{ta_sk.name}--{ta_sk.due_date}")
            sleep(1)
            
      
    #inserts the index of the task that he wants to complete
    def complete_task(self,index_task):
        if index_task == 0 :
            return
        
        #if the user has put a number that doesn't agree with the statement the he will receive an error message
        
        if 1 <= index_task <= len(self.tasks)-1:
           tak = self.tasks[index_task-1]
           tak.complete_the_task()
           print(f"{tak} is Completed")
           print("-"*40)
           self.tasks.remove(tak)
           sleep(2)
           return 
        print("Index out of bounts")    
        sleep(2)
        os.system("cls")
        return
# A logo for the Task Managment Project            
def print_task_management_logo():
    logo = """
    ██████╗  █████╗ ████████╗███████╗    ███████╗██╗██╗   ██╗███████╗
    ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝    ██╔════╝██║╚██╗ ██╔╝██╔════╝
    ██████╔╝███████║   ██║   █████╗      █████╗  ██║ ╚████╔╝ █████╗  
    ██╔══██╗██╔══██║   ██║   ██╔══╝      ██╔══╝  ██║  ╚██╔╝  ██╔══╝  
    ██║  ██║██║  ██║   ██║   ███████╗    ██║     ██║   ██║   ███████╗
    ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝    ╚═╝     ╚═╝   ╚═╝   ╚══════╝
    -----------------------------------------------------------------
    """
    print(logo)


task_manager = Task_Managment()
#the starting screen of the user
def first_screen():
    
    print("1.View Tasks")
    print("2.Create Task")
    print("3.Exit")
    
choice = ""
while True:
    
    print_task_management_logo()
    
    #viewing the first screen 
    #1.View Tasks 
    #2.Create Task
    #3.Exit
    
    
    first_screen()
    choice = input("Enter choice: ")
    
    # if statement if the user puts the answer that we want him to put 
    #otherwise it shows him a message that he had put a wrong input
    if choice in ["1","2","3"]:
       
       # if choice is 3 then the program terminates
       
       if choice == "3":
           print("Terminating...")
           sys.exit()
       elif choice == "1":
           if task_manager.tasks:
               
               task_manager.view_tasks()
               
               sleep(1)
               #if he hasn't completed any task or doesn't want to mark it he has to press 0
               print("press 0 if you don't want to complete a task")
               
               answer = input("Enter index of Task to Complete: ")
               
               #calls the function complete_task 
               task_manager.complete_task(int(answer))
           else:
               print("There are not available task at this moment")
               sleep(1)
           os.system("cls")
       else:
           
           #if the user press 2 then he will have to put the task that he wants with a name,description , due_date
           
           name = input("Enter the name of the Task: ")
           description = input("(optional) Enter description of the Task: ")
           date_string = input("Enter due date (DD-MM-YYYY): ")
           due_date = datetime.strptime(date_string,"%d-%m-%Y")
           new_task = Task(name,description,due_date)
           task_manager.add_task(new_task)
           print("Task Added!")  
           sleep(2)
           os.system("cls")
    else:
      print("Wrong Input please Try Again!")  
      sleep(1)
      os.system("cls")    

     
    
     

    
    