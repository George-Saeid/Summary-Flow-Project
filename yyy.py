# Check if the number is divisible by 2 or 3
def divide_number(number):
    if number == 1 or number == 2 or number == 3:
        return number,  # Return a tuple with a single element
    if number % 3 == 0 or number % 2 == 0:
        return number,  # Return a tuple with a single element
    else:
        # Start values
        large_part = number - 2
        small_part = 2
        # Find two valuse divisible by 2 or 3 there sum equals the input number
        while True:
            if (large_part % 3 == 0 or large_part % 2 == 0) and (small_part % 3 == 0 or small_part % 2 == 0):
                # The two values were found
                break
            else:
                large_part -= 1
                small_part += 1
        return large_part, small_part


# Test the function with numbers from 1 to 1000
for x in range(1, 1001):
    result = divide_number(x)
    if len(result) == 1:
        num1 = result[0]
        print(f"The number {num1} is divisible by 2 or 3")
    else:
        num1, num2 = result
        print(f'The number {x} can be divided into: {num1} and {num2}')