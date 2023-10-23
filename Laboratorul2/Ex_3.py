def list_operations(a, b):
    intersection = list(set(a) & set(b))
    union = list(set(a) | set(b))
    difference_a = list(set(a) - set(b))
    difference_b = list(set(b) - set(a))
    return intersection, union, difference_a, difference_b


def main():
    a = [1, 2, 3, 4, 5]
    b = [3, 4, 5, 6, 7]
    intersection, union, difference_a, difference_b = list_operations(a, b)
    print("Intersection:", intersection)
    print("Union:", union)
    print("a-b:", difference_a)
    print("b-a:", difference_b)


main()
