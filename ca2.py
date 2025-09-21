#wap to create largest possible no using the elements of a given list of positive integers.

list=[10,20,30]
a=list[0]+list[1]
b=list[0]+list[2]
c=list[1]+list[0]
d=list[1]+list[2]

if a>b or a>c or a>d:
    print(a," it is the largest possible no")
elif b>a or b>c or b>d:
    print(b," it is the largest possible no")
elif c>a or c>b or c>d:
    print(c,"it is the largest possible no")



#wap to create a dictionary of keys x,y and z where each key have a value list from 11-20,21-30 and 31-40 access the fifth value from each key from dict.

dict1={'x':[11,12,13,14,15,16,17,18,20],
       'y':[21,22,23,24,25,26,27,28,29,30],
       'z':[31,32,33,34,35,36,37,38,39,40]}

print(dict1['x'][4])
print(dict1['y'][4])
print(dict1['z'][4])
