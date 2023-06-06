def two_sum(nums, target):
    # Create a dictionary to store the complement of each number
    complement_dict = {}

    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement
        complement = target - num

        # Check if the complement exists in the dictionary
        if complement in complement_dict:
            # Return the indices of the current number and its complement
            return [complement_dict[complement], i]

        # Add the current number and its index to the dictionary
        complement_dict[num] = i

    # If no solution is found, return an empty list or raise an exception
    return []


nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1] 
