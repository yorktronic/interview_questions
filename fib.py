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

# My slowest
def fibonacci_faster(n):
    sequence = [0] * n

    for idx, num in enumerate(sequence):
        if idx == 0:
            sequence[idx] = 0
        elif idx == 1:
            sequence[idx] = 1
        else:
            sequence[idx] += sequence[idx - 1] + sequence[idx - 2]

    return sequence

# Optimal
def fibo(n):
    a, b = 0, 1
    for i in xrange(n):
        yield a
        a, b = b, a + b

def generate(n):
    return list(fibo(n))
