# 1. Write a python script to reverse a number

def reverse_number(number):
    reversed_number = 0

    while number > 0:
        # Get the last digit of the number
        digit = number % 10

        # Append the digit to the reversed number
        reversed_number = (reversed_number * 10) + digit

        # Remove the last digit from the number
        number = number // 10

    return reversed_number


# Test the function
number = int(input("Enter a number: "))
reversed_number = reverse_number(number)
print("Reversed number:", reversed_number)
