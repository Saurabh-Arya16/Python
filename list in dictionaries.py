#program for lists in dictionaries

st_records={
    1:{'name':'Alice','grades':[85,90,78]},
    2:{'name':'Bob','grades':[92,88,95]},
    3:{'name':'Charlie','grades':[70,75,80]}
}

print("Student Records:")
for sid,details in st_records.items():
    print(f"ID:{sid},Name:{details['name']},Grades:{details['grades']}")

print("\n Average grades:")
for sid in st_records:
    grades=st_records[sid]['grades']
    average=sum(grades)/len(grades) if grades else 0
    print(f"Student ID:{sid},Average Grade:{average:.2f}")