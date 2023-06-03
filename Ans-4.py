# Write a python script to print all Prime numbers between two given numbers (both values inclusive)
def is_prime(number):
    if number <= 1:
        return False

    # Check for factors from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


# Get the range from the user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Prime numbers between", start, "and", end, "are:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num)

