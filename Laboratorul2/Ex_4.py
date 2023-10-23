def compose(notes, moves, start_position):
    song = []
    current_position = start_position

    for move in moves:
        current_position += move

        # Ensure the current position is within the bounds of the notes list
        current_position %= len(notes)

        song.append(notes[current_position])

    return song


def main():
    notes = ["do", "re", "mi", "fa", "sol"]
    moves = [1, -3, 4, 2]
    start_position = 2
    song = compose(notes, moves, start_position)
    print(song)


main()
