def move_zeros(nums):
    # Initialize two pointers
    left = 0  # Points to the position to be filled with a non-zero element
    right = 0  # Points to the current element being considered

    # Iterate through the array
    while right < len(nums):
        # If the current element is non-zero, move it to the left pointer position
        if nums[right] != 0:
            nums[left] = nums[right]
            left += 1

        # Move the right pointer to the next element
        right += 1

    # Fill the remaining elements with zeros
    while left < len(nums):
        nums[left] = 0
        left += 1


nums = [0, 1, 0, 3, 12]
move_zeros(nums)
print(nums) 
