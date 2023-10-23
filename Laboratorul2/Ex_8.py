def filter_characters(x, strings, flag):
    result = []

    for s in strings:
        char_list = []

        for char in s:
            ascii_code = ord(char)
            if (ascii_code % x == 0) if flag else (ascii_code % x != 0):
                char_list.append(char)

        result.append(char_list)

    return result


def main():
    x = 2
    strings = ["test", "hello", "lab002"]
    flag = False
    filtered_lists = filter_characters(x, strings, flag)
    print(filtered_lists)


main()
