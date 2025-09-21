#Program of using list in addition to "for" loop

student_names=["Alice","Bob","Charlie"]
student_grades=[85,92,78]

print("Initial list of students:")
for name,grade in zip(student_names,student_grades):
    print(f"{name}:{grade}")

new_name="David"    
new_grade=88
student_names.append(new_name)
student_grades.append(new_grade)

print("\n Adding a new student 'David' with grade 88:")
for name,grade in zip(student_names,student_grades):
    print(f"{name}:{grade}")