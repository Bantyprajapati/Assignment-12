#  Write a python script to print first N terms of a Fibonacci series
def fibonacci_series(n):
    series = []
    
    # Handle the base cases
    if n >= 1:
        series.append(0)
    if n >= 2:
        series.append(1)
    
    # Generate the Fibonacci series
    for i in range(2, n):
        next_term = series[i - 1] + series[i - 2]
        series.append(next_term)
    
    return series


# Test the function
n = int(input("Enter the value of N: "))
fibonacci_terms = fibonacci_series(n)
print("First", n, "terms of the Fibonacci series are:", fibonacci_terms)
