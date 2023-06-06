def plus_one(digits):
    # Start from the rightmost digit
    i = len(digits) - 1

    # Iterate through the digits from right to left
    while i >= 0:
        # If the current digit is less than 9, increment it by one and return the digits
        if digits[i] < 9:
            digits[i] += 1
            return digits

        # If the current digit is 9, set it to 0 and continue to the next digit
        digits[i] = 0
        i -= 1

    # If all digits are 9, add an additional digit of 1 at the beginning
    return [1] + digits

  
digits = [1, 2, 3]
result = plus_one(digits)
print(result)  # Output: [1, 2, 4] 
