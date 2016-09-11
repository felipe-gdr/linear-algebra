"""Count words."""

def count_words(s, n):
    """Return the n most frequently occuring words in s."""

    # TODO: Count the number of occurences of each word in s
    words = s.split(' ')
    d = {}
    for w in words:
        if w in d:
            d[w] = d[w] + 1
        else:
            d[w] = 1

    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    result = []
    [result.append(v) for v in sorted(d.items(), key=lambda kv: (-kv[1], kv[0]))]

    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    return result[:n]


def test_run():
    """Test count_words() with some inputs."""
    print (count_words("cat bat mat cat bat cat", 3))
    print (count_words("betty bought a bit of butter but the butter was bitter", 3))


if __name__ == '__main__':
    test_run()
