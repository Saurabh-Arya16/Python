my_list = [1, 25, 56, 42, 30]

max_product = float('-inf')

for i in range(len(my_list) - 1):  
    product = my_list[i] * my_list[i + 1]
    
    if product > max_product:
        max_product = product

print(f"Maximum product of  any two consecutive number in the list: {max_product}")
