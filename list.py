#program to simple basic list elements and accesing them

my_list=[1,2,3,4,5]
print(my_list)
print(my_list[0])

print(my_list[-1])
my_list.append(6)
print(my_list)
my_list.insert(2,'new')
print(my_list)

my_list.remove('new')
print(my_list)