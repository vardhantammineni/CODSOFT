tasks=[]

def add_task():
    task=input("Enter task:")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(i+1,".",tasks[i])
            
def remove_task():
    if not tasks:
        print("No Tasks to Remove.")
    else:
        view_tasks()
        num=int(input("Enter task number to remove:"))
        removed=tasks.pop(num-1)
        print("Removed:",removed)
        
def menu():
    print("\n**** TO_DO LIST ****")
    print("1.Add Task")
    print("2.View Tasks")
    print("3.Remove Task")
    print("4.Exit")
    
while True:
    menu()
    choice=input("Enter your choice:")
    
    if choice=="1":
        add_task()
    elif choice=="2":
        view_tasks()
    elif choice=="3":
        remove_task()
    elif choice=="4":
        print("Thank You!")
        break
    
else:
    print("Invalid Choice!")
    
   