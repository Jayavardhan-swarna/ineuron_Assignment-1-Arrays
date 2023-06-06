def contains_duplicate(nums):
    num_set = set()

    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)

    return False

# Test the function
nums = [1, 2, 3, 1]
result = contains_duplicate(nums)
print(result)  # Output: True 
