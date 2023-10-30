def count_characters(text):
    characters_count = {}
    for char in text:
        if char in characters_count:
            characters_count[char] += 1
        else:
            characters_count[char] = 1

    return characters_count


def main():
    text = "Ana has apples"
    result = count_characters(text)
    print(result)


main()
