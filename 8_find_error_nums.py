def find_error_nums(nums):
    n = len(nums)

    # Find the duplicate number
    duplicate = -1
    num_set = set()
    for num in nums:
        if num in num_set:
            duplicate = num
            break
        num_set.add(num)

    # Calculate the missing number
    missing = sum(range(1, n+1)) - sum(nums) + duplicate

    return [duplicate, missing]


nums = [1, 2, 2, 4]
result = find_error_nums(nums)
print(result)   
