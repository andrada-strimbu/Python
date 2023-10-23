def is_palindrome(number):
    return str(number) == str(number)[::-1]


def find_palindromes(numbers):
    palindrome_count = 0
    greatest_palindrome = None

    for number in numbers:
        if is_palindrome(number):
            palindrome_count += 1
            if greatest_palindrome is None or number > greatest_palindrome:
                greatest_palindrome = number

    return palindrome_count, greatest_palindrome


def main():
    numbers = [121, 12321, 12345, 131, 45654, 789]
    result = find_palindromes(numbers)
    print("Number of palindromes:", result[0])
    print("Greatest palindrome:", result[1])


main()
