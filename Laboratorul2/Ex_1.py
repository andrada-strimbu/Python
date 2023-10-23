def generate_fibonacci(n):
    if n <= 0:
        return []

    fibonacci_sequence = [0]
    if n == 1:
        return fibonacci_sequence

    fibonacci_sequence.append(1)

    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence


def main():
    n = 10
    result = generate_fibonacci(n)
    print(result)


main()
