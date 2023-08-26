import itertools

def numTilePossibilities(tiles: str) -> int:
    counter = 0

    for i in range(1, len(tiles) + 1):
        permutations = list(itertools.permutations(tiles, i))
        perm_set = set(permutations)
        counter += len(perm_set)

    return counter


if __name__ == '__main__':
    assert(numTilePossibilities("AAB")) == 8
    assert(numTilePossibilities("AAABBC")) == 188
    assert(numTilePossibilities("V")) == 1
