# Write a python script to calculate LCM of two numbers
def calculate_lcm(num1, num2):
    # Find the maximum of the two numbers
    max_num = max(num1, num2)

    # Start with the maximum number and check if it is divisible by both numbers
    lcm = max_num
    while True:
        if lcm % num1 == 0 and lcm % num2 == 0:
            break
        lcm += max_num

    return lcm


# Test the function
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

lcm = calculate_lcm(num1, num2)
print("The LCM of", num1, "and", num2, "is", lcm)
