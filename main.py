def cmmdc(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def count_vowels(input_string):
    input_string = input_string.lower()
    vowels = "aeiou"
    vowel_count = 0
    for char in input_string:
        if char in vowels:
            vowel_count += 1
    return vowel_count

def count_occurrences(substring, full_string):
    count = 0
    index = 0
    while index < len(full_string):
        index = full_string.find(substring, index)
        if index == -1:
            break
        count += 1
        index += len(substring)
    return count
def convert_to_lower_with_underscores(input_string):
    converted_string = ''
    for char in input_string:
        if char.islower() or char.isdigit():
            converted_string += char
        elif char.isupper():
            converted_string += '_' + char.lower()
    return converted_string


def is_palindrome_number(num):
    num_str = str(num)
    return num_str == num_str[::-1]

def extract_first_number(text):
    number = ""
    found_digit = False

    for char in text:
        if char.isdigit():
            number += char
            found_digit = True
        elif found_digit:
            break

    if number:
        return int(number)
    else:
        return None

def count_set_bits(number):
        count = 0
        while number:
            count += number & 1
            number >>= 1
        return count

def most_common_letter(text):
    text = text.lower()
    letter_count = {}

    for char in text:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    most_common = max(letter_count, key=letter_count.get)

    return most_common, letter_count[most_common]

def count_words(text):
    words = text.split()
    return len(words)

def main():

    #pb1
    a = int(input("a: "))
    b = int(input("b: "))
    f_cmd = cmmdc(a, b)
    print(f'Cmmdc este: {f_cmd}')
    #pb2
    user_input = input("Introduceți un sir: ")
    vowel_count = count_vowels(user_input)
    print(vowel_count)
    #pb3
    first_string = input("Introduceți primul șir: ")
    second_string = input("Introduceți al doilea șir: ")
    occurrences = count_occurrences(first_string, second_string)
    print(f"Numărul de apariții: {occurrences}")
    #pb4
    input_string = input("Introduceți un sir UpperCamelCase: ")
    converted_string = convert_to_lower_with_underscores(input_string)
    print( converted_string)
    #pb6
    palindrom = is_palindrome_number(12321)
    print(palindrom)
    #pb8
    number = int(input("Introduceti un numar: "))
    bit_count = count_set_bits(number)
    print(bit_count)
    #pb9
    text = "an apple is not a tomato"
    common_letter, count = most_common_letter(text)
    print(f"{common_letter} ({count} ori).")
    #pb10
    word_count = count_words(text)
    print(f"Numarul de cuvinte: {word_count}")

main()

