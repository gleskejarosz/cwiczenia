def numJewelsInStones(jewels, stones):
    count = 0
    for j in jewels:
        for s in stones:
            if s == j:
                count += 1
    return count


if __name__ == '__main__':
    assert(numJewelsInStones("aA", "aAAbbbb")) == 3
    assert (numJewelsInStones("z", "ZZ")) == 0
