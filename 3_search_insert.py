def search_insert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # If the target is not found, return the left pointer
    return left


nums = [1, 3, 5, 6]
target = 5
index = search_insert(nums, target)
print(index)  
