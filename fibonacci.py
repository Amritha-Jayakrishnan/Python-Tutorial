# Fibonacci Series
# Prints the Fibonacci sequence up to n terms

def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

n = int(input("Enter number of terms: "))
print("Fibonacci Series:", fibonacci(n))
