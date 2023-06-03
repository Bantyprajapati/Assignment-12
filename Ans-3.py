# Write a python script to print all Prime numbers under 100

def is_prime(number):
    if number <= 1:
        return False

    # Check for factors from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


print("Prime numbers under 100:")
for num in range(2, 100):
    if is_prime(num):
        print(num)
