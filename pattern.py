#program to print Equilateral triangle

height=5
for i in range(height):
    row=''*(height-i-1)+'*'*(2*i+1)
    print(row)
