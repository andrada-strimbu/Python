def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1): #pana la radical din n
        if n % d == 0:
            return False
    return True


def find_prime_numbers(numbers):
    prime_numbers = []
    for number in numbers:
        if is_prime(number):
            prime_numbers.append(number)
    return prime_numbers


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = find_prime_numbers(numbers)
    print(result)


main()