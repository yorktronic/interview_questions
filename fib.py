# Write a function that takes a number n and returns an array
# containing a Fibonacci sequence of length

# My fastest
def fibonacci(n):
    i = 2
    sequence = [0, 1]
    while i < n:
        sequence.append(sequence[-1] + sequence[-2])
        i += 1

    return sequence

# Optimal
def fibo(n):
    a, b = 0, 1
    for i in xrange(n):
        yield a
        a, b = b, a + b

def generate(n):
    return list(fibo(n))
