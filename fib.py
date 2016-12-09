# Write a function that takes a number n and returns an array
# containing a Fibonacci sequence of length

def fibonacci(n):
    i = 2
    sequence = [0, 1]
    while i < n:
        sequence.append(sequence[-1] + sequence[-2])
        i += 1

    return sequence

