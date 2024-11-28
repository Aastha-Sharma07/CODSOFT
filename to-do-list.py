print("----WELCOME TO THE TO DO LIST----")
Task = []
def task_list():
    create_task = int(input("How many tasks you want to do ="))
    
    for j in range(1,create_task+1):
        name = input(f"Enter task {j}:")
        Task.append(name) 
        
        print(f"Your task {name} added successfully")
    print(f"Your tasks are \n{Task}")

    #To update and track tasks
    while True:
        operation = int(input("\nTo UPDATE task name, enter number 1 \n To VIEW task list, enter number 2 \n To TRACK task list, enter number 3 \n To EXIT, enter number 0 \n Enter your number please="))
    
        if operation==1:
            up_task = input("Enter task name that you want to want update:")
            if up_task in Task:
                new_task = input("Enter new task name:")
                z = Task.index(up_task)
                Task[z]=new_task
                print("Updated task.....")
                print(f"Your task {new_task} has been updated.")
            else:
                print("Invalid input")
        
        elif operation == 2:
            print(f"All the tasks that you have to do are {Task}")

        elif operation==3:
            Completed_task = []
            comp_task = input("Enter the task name that you had completed:")
            if comp_task in Task:
                Completed_task.append(comp_task)
                print(f"Completed tasks = {Completed_task}")
            else:
                print("This task is not in your list")

        elif operation == 0:
            print("THANK YOU")
            break
        else:
            print("Invalid input")
            
task_list()
