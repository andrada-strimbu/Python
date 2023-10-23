def items_appearing_x_times(x, *lists):
    # Create a dictionary to count the occurrences of each item
    item_counts = {}

    # Iterate through each list and count the occurrences of items
    for lst in lists:
        for item in lst:
            if item in item_counts:
                item_counts[item] += 1
            else:
                item_counts[item] = 1

    # Filter items that appear exactly x times
    result = [item for item, count in item_counts.items() if count == x]

    return result


def main():
    list1 = [1, 2, 3]
    list2 = [2, 3, 4]
    list3 = [4, 5, 6]
    list4 = [4, 1, "test"]
    x = 2

    result = items_appearing_x_times(x, list1, list2, list3, list4)
    print(result)


main()
