# Write a python script to print first N prime numbers
def is_prime(number):
    if number <= 1:
        return False

    # Check for factors from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def print_first_n_primes(n):
    primes = []
    num = 2  # Start checking from 2

    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1

    return primes


# Test the function
n = int(input("Enter the value of N: "))
first_n_primes = print_first_n_primes(n)
print("First", n, "prime numbers are:", first_n_primes)
