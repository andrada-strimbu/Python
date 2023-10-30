def count_unique_and_duplicate_elements(input_list):
    unique_elements = set()
    element_counts = {}
    for item in input_list:
        if item in unique_elements:
            element_counts[item] = element_counts.get(item, 0) + 1
        else:
            unique_elements.add(item)

    b = sum(element_counts.values())
    a = len(unique_elements)
    return a, b


def main():
    my_list = [1, 2, 2, 3, 4, 4, 5, 6]
    result = count_unique_and_duplicate_elements(my_list)
    print(result)


main()
