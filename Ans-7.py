# Write a python script to check whether a given pair of numbers are co-Prime numbers or not
def are_coprime(a, b):
    # Find the greatest common divisor (GCD) of the two numbers
    while b != 0:
        a, b = b, a % b

    # If the GCD is 1, the numbers are coprime; otherwise, they are not
    if a == 1:
        return True
    else:
        return False


# Test the function
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if are_coprime(num1, num2):
    print(num1, "and", num2, "are co-prime numbers")
else:
    print(num1, "and", num2, "are not co-prime numbers")
