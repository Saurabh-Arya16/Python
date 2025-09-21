#dictionary example

data={
    'a':1,
    'b':2,
    'c':3,
    'e':2
}

to_remove=1

keys_to_remove=[key for key,value in data.items() if value==to_remove]

for key in keys_to_remove:
    del data[key]
    print(data)

#Write a program that takes two dictionaries and returns a list of keys that are present in both dictionaries.
first={'car':'mahindra','bike':'honda','cycle':'hero'}
second={'soap':'dove','paste':'colgate','bike':'honda'}

both=first.keys() & second.keys()
print(f"common key in both dictionary were{both}")

#Write a program that takes a dictionary and a value, and returns the key associated with that value. If the value is not found, return None.

take = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
user = take
target = input("Enter the value to find: ")

found = False
for key, value in user.items():
    if value == target:
        print(key)
        found = True
        break

if not found:
    print(None)

#write a program to structure nested dictionary to store information of employees including their names,position and departments

employee={'Tarun':{'position':'developer','department':'programming'},
          'varun':{'positon':'manager','department':'Sales'},
          'Aj':{'position':'headmaster','department':'production'}}

for key,details in employee.items():
   print(f"Employee name:{key}")

   for detail_key,detail_value in details.items():
        print(f"{detail_key.capitalize()}: {detail_value}")

#write a program to create two dictionaries containing same keys but different values.Demonstrate how would you combine them to single dictionary

dict1={1:'a',2:'b',3:'c'}
dict2={1:'d',2:'e',3:'f'}

combined_dict={}
for key in dict1.keys():
    combined_dict[key]=[dict1[key],dict2[key]]

    print(combined_dict)


#write on program to have list of students name and their corresponding grades,construct a dictionary that maps each student name with their grades

students=["Alice","Bob","Charlie","David","Eve"]
grades=[85,92,78,90,88]

student_grades={}
for i in range(len(students)):
    student_grades[students[i]]=grades[i]

    print(student_grades)






