def order_tuples_by_third_char(tuples):
    sorted_tuples = sorted(tuples, key=lambda x: x[1][2])
    return sorted_tuples


def main():
    tuples = [('abc', 'bcd'), ('abc', 'zza')]
    sorted_tuples = order_tuples_by_third_char(tuples)
    print(sorted_tuples)


main()
