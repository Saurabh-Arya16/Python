#"""Program to find number of chickens and rabbits
head = 35
legs = 94
chickens = 0
while True:
    rabbits = head - chickens
    if (2*chickens + 4*rabbits) == 94:
        print(f"Chickens = {chickens}")
        print(f"rabbits = {rabbits}")
        break
    else:
        chickens +=1