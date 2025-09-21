print("To-do-list")
task=None
while True:
    print("\n New")
    print("1,Add task")
    print("2,view task")
    print("3,Remove task")
    print("4,Exit")
    
    choice=input("Enter choice(1/2/3/4:)")

    if choice=="4":
        print("Exiting the to-do-list manager")
        break

    if choice=="1":
        task=input("enter the task to add:")
        print(f"Task added",{task})

    elif choice=="2":
        if task:
            print(f"current task",{task})
        else:
            print("no task in the to do list")
    elif choice=="3":
        if task:
            print(f"removed task",{task})
            task=None
        else:
            print("no task to remove")
    else:
        print("Invalid choice,please enter a number between 1 to 4")
    

        
