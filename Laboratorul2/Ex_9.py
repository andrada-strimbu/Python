def find_seats_with_obstructed_view(heights):
    obstructed_seats = []
    num_rows = len(heights)
    num_cols = len(heights[0])

    for j in range(num_cols):
        max_h = 0
        for i in range(num_rows):
            if heights[i][j] > max_h:
                max_h = heights[i][j]
            else:
                obstructed_seats.append((i, j))

    return obstructed_seats


def main():
    stadion = [
        [1, 2, 3, 2, 1, 1],
        [2, 4, 4, 3, 7, 2],
        [5, 5, 2, 5, 6, 4],
        [6, 6, 7, 6, 7, 5]
    ]

    rezultat = find_seats_with_obstructed_view(stadion)
    print(rezultat)


main()
