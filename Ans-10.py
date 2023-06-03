#  Write a python script to calculate HCF of two numbers
def calculate_hcf(num1, num2):
    # Find the smaller number between the two
    min_num = min(num1, num2)

    # Iterate from the smaller number down to 1 and find the largest number that divides both numbers
    hcf = 1
    for i in range(1, min_num + 1):
        if num1 % i == 0 and num2 % i == 0:
            hcf = i

    return hcf


# Test the function
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

hcf = calculate_hcf(num1, num2)
print("The HCF of", num1, "and", num2, "is", hcf)
