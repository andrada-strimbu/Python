def set_operations(*sets):
    operations = {
        "union": "|",
        "intersection": "&",
        "difference": "-"
    }

    result_dict = {}
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            set_a = sets[i]
            set_b = sets[j]

            for op_name, op_symbol in operations.items():
                key = f"{set_a} {op_symbol} {set_b}"
                if op_name == "union":
                    result = set_a | set_b
                elif op_name == "intersection":
                    result = set_a & set_b
                elif op_name == "difference":
                    result = set_a - set_b

                result_dict[key] = result

    return result_dict


def main():
    set1 = {1, 2}
    set2 = {2, 3}
    result = set_operations(set1, set2)
    print(result)


main()
