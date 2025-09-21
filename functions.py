def modify_list(input_list):
    input_list.append(10)
    return input_list

def main():
    my_list = [1, 2, 3, 4, 5]
    print("Original list:", my_list)
    modified_list = modify_list(my_list)
    print("Modified list:", modified_list)
    #print(f"modified list:{modify_list(my_list)}")

if __name__ == "__main__":
    main()

#program of default argument or default parameter

def calculate(amount,discountPercentage=0):
    discountAmount=discountPercentage/100*amount
    return amount-discountAmount

amount=500
totalbillAmount=calculate(amount,10)
print(totalbillAmount)

amount=500
totalbillAmount=calculate(amount)
print(totalbillAmount)

#Write a function that takes a list of strings and returns a dictionary where the keys are the unique strings and the values are the counts of their occurrences in the list.
def count_occurrences(input_list):
    occurrences_dict = {}
    for string in input_list:
        if string in occurrences_dict:
            occurrences_dict[string] += 1
        else:
            occurrences_dict[string] = 1
    return occurrences_dict

input_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(count_occurrences(input_list))

#Create a function that converts a dictionary into a list of tuples. Each tuple should contain a key-value pair from the dictionary.
def dict_to_tuples(input_dict):
    return list(input_dict.items())

example_dict = {'apple': 3, 'banana': 2, 'orange': 1}
print(dict_to_tuples(example_dict))

#another function program
def add_numbers(*args):
    return sum(args)

print(add_numbers(1,2,3,4))

#list,dictionary
def process_data(list_input, dict_input):
    squared = [x**2 for x in list_input]

    incremented = {key: value + 1 for key, value in dict_input.items()}

    return squared, incremented

if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5]
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    
    sq_list, processed_dict = process_data(list1, dict1)

    print("Processed List:", sq_list)
    print("Processed Dictionary:", processed_dict)

#Write a function reverse_string() that takes a string and returns it reversed.
def reverse_string(a):
    for i in reversed(a):
        print(i)

a="hello world"
c=reverse_string(a)
print(c)
#Write a function that takes a dictionary of students and their grades, calculates the average grade, and returns a new dictionary with students who have grades above the average. The function should accept a dictionary in the following format:

def above_average(students):
    total = 0
    count = 0
    
    for grades in students.values():
        total += sum(grades)
        count += len(grades)
        
    average_grade = total / count if count > 0 else 0
    print(f"Average grade: {average_grade}")
    
    above_avg = {}
    for student, grades in students.items():
        student_average = sum(grades) / len(grades) if grades else 0
        if student_average > average_grade:
            above_avg[student] = grades
    
    return above_avg

# Main function execution
if __name__ == "__main__":
    students = {
        "Abc": [85, 90, 78],
        "Xyz": [70, 75, 80],
        "Pqr": [95, 92, 88]
    }
    result = above_average(students)
    print("Students with above-average grades:", result)

#Write a program for to-do list.How would you modify the add_task function to prevent adding duplicate tasks to the list?
#How does the program respond if you attempt to display the to-do list when it is empty?
def add_task(task):
    return input("Enter the task to add: ")

def view_task(task):
    if task:
        print(f"Current task: {task}")
    else:
        print("No task in the to-do list")

def remove_task(task):
    if task:
        print(f"Removed task: {task}")
        return None
    else:
        print("No task to remove")
    return task

def main():
    print("To-do-list")
    task = None
    
    while True:
        print("\nNew")
        print("1. Add task")
        print("2. View task")
        print("3. Remove task")
        print("4. Exit")
        
        choice = input("Enter choice (1/2/3/4): ")
        
        if choice == "4":
            print("Exiting the to-do-list manager")
            break
        elif choice == "1":
            task = add_task(task)
            print(f"Task added: {task}")
        elif choice == "2":
            view_task(task)
        elif choice == "3":
            task = remove_task(task)
        else:
            print("Invalid choice, please enter a number between 1 to 4")

if __name__ == "__main__":
    main()

