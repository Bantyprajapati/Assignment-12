# Write a python script to find next prime number of a given number
def is_prime(number):
    if number <= 1:
        return False

    # Check for factors from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def find_next_prime(number):
    next_number = number + 1

    while True:
        if is_prime(next_number):
            return next_number
        next_number += 1


# Test the function
number = int(input("Enter a number: "))
next_prime = find_next_prime(number)
print("The next prime number after", number, "is", next_prime)
