def combine_lists(*lists):
    max_length = max(len(lst) for lst in lists)
    combined = []

    for i in range(max_length):
        tuple_elements = tuple(lst[i] if i < len(lst) else None for lst in lists)
        combined.append(tuple_elements)

    return combined


def main():
    list1 = [1, 2, 3]
    list2 = [5, 6, 7]
    list3 = ["a", "b", "c"]
    result = combine_lists(list1, list2, list3)
    print(result)


main()
