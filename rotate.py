def rotate_list(nums, k):
    k = k % len(nums)
    
    return nums[-k:] + nums[:-k]

nums = [1, 2, 3, 4, 5]
k = 2
rotated_list = rotate_list(nums, k)
print(rotated_list)
