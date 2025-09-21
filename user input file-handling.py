#user-input file handling

def write_content(filename):
    file=open(filename,'w')
    print("Enter content to write to the file(type 'EXIT'to stop):")

    while True:
        user_input=input()

        if user_input=="EXIT" or user_input=="Exit" or user_input=="exit":
            break

        file.write(user_input + '\n')
        file.close()
        print(f"Content has been written to {filename}")

filename='input.txt'        
write_content(filename)

def read_content(filename):
    file=open(filename,'r')
    content=file.read()
    file.close()

    print("Content read from the file:")
    print(content)

filename='input.txt'    
read_content(filename)

#another program of file handling

tasks = ["Buy groceries", "Read a book", "Write Python code"]
with open('tasks.txt', 'w') as file:
    for task in tasks:
        file.write(task + "\n")
        print("Tasks written to tasks.txt.")


try:
    with open('tasks.txt', 'r') as file:
        tasks = file.readlines()
        tasks = [task.strip() for task in tasks]
        print("Tasks read from tasks.txt:")
        print(tasks)
        
except FileNotFoundError:
    print("The file does not exist.")