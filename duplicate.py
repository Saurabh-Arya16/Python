def remove_duplicates(lst):
    seen = set()  # To store elements we've encountered
    result = []   # To store the final list without duplicates

    for item in lst:
        if item not in seen:
            result.append(item)  # Add the item to the result if not seen before
            seen.add(item)       # Mark the item as seen

    return result

# Example usage
lst = [1, 2, 2, 3, 4, 4, 5]
unique_lst = remove_duplicates(lst)
print(unique_lst)
