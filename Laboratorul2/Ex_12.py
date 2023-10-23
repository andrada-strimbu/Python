def group_by_rhyme(words):
    rhyme_groups = {}

    for word in words:
        ending = word[-2:]
        if ending not in rhyme_groups:
            rhyme_groups[ending] = []
        rhyme_groups[ending].append(word)
    grouped_words = list(rhyme_groups.values())
    return grouped_words


def main():
    words = ['ana', 'banana', 'carte', 'arme', 'parte']
    result = group_by_rhyme(words)
    print(result)


main()
