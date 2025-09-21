#new program
def add_task(tasks, task):
    tasks.append(task)
    print(f"Added task: {task}")

def remove_task(tasks, task):
    if task in tasks:
        tasks.remove(task)
        print(f"Removed task: '{task}'")
    else:
        print(f"Task '{task}' not found in the to-do list")

def display_tasks(tasks):
    if tasks:
        print("Current to-do list:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("The to-do list is empty.")

if __name__ == "__main__":
    to_do_list = []
    add_task(to_do_list, "Buy groceries")
    add_task(to_do_list, "Walk the dog")
    display_tasks(to_do_list)
    remove_task(to_do_list, "Buy groceries")
    display_tasks(to_do_list)
    remove_task(to_do_list, "Clean the house")
    display_tasks(to_do_list)

#wap to define function that accecpts dictionary as an argument and returns a list of its keys
def function(dict1):
    return list(dict1.keys())
dict1={'name':'aj','work':'dj','office':'punjab'}
print(function(dict1))


#write a function that take two sets and returns the  their intersection as a new set
def intersection(a,b):
    return a & b

a={1,2,3,4,5}
b={4,5,6,7,8}
c=intersection(a,b)
print(c)

#implement a function that take 2 dictionaries and returns a new dictionary that contain all keys from both dictionaries.
# If key exits in both dictionaries that value in first dictionary should be used.
def new(first,second):
    return dict(first|second)

first={'name':'dj','class':10,'gender':'male'}
second={'toy':'lego','comic':'marvel','game':'gta'}
third=new(first,second)
print(third)

#implement the function that checks if all keys of given dictionary exists in the list.if all keys are present return True else return false

cmds={}
dv=[]