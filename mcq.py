#mcq for python
for i in range(5):
    if i==3:
        continue
    print(i,end='')

s="Python Programming"
print(s[7:17])

my_list=[1,2,4,5,6]
my_list[1:4]=[10,20]
print(my_list)

t=[1,2,3,4]
print(t[1:3])

x=[1,2,3]
y=x
y[0]=10
print(x)

x=0
while x<3:
    x+=1
    if x==2:
        break
    print(x,end='')

s="hello world"
s=s.replace("world","Python")
print(s)





list1=[1,2,3]
list2=list1*2
print(list2)


t=(1,2,3,4,5)
print(t[-2:])


a="hello"
b="world"
c=a+""+b
print(len(c))


my_list=[1,2,3,4]
my_list.pop(2)
print(my_list)

a=3*(2+5)/4-1
print(a)

b=8+2*5-3/1
print(b)

c=(6+4)*2**2
print(c)

d=9/3+2*(5-1)
print(d)