#write a python program to create menu where dishes(keys) and prices(values)that:

menu={'cake':150,'chocolate':10,'bun':200}
print(menu)

#adds a new dish and its price to the dictionary.
menu['cupcake']=150
print(menu)

#updates the price of an existing dish.
menu['bun']=170
print(menu)

#uses a for loop to display all dishes that cost more than $10

keys=menu.keys()
for i in keys:
        print(i)