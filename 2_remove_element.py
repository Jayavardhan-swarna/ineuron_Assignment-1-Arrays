def remove_element(nums, val):
    # Initialize two pointers
    i = 0  # Slow pointer
    j = 0  # Fast pointer

    # Iterate through the array
    while j < len(nums):
        # If the current element is not equal to val, move it to the slow pointer position
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1

        # Move the fast pointer to the next element
        j += 1

    # Return the number of elements remaining (k)
    return i


nums = [3, 2, 2, 3]
val = 3
k = remove_element(nums, val)
print(k)  
print(nums[:k])  
