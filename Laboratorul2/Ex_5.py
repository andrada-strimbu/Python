def replace_below_main_diagonal(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for i in range(num_rows):
        for j in range(num_cols):
            if i > j:
                matrix[i][j] = 0

    return matrix


def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    result = replace_below_main_diagonal(matrix)
    for row in result:
        print(row)

main()