def minimumRecolors(blocks: str, k: int) -> int:
    blocks_len = len(blocks)
    indexes = []

    for idx, block in enumerate(blocks):
        if block == "W":
            indexes.append(idx)

    min_count = blocks_len
    temp_count = 0

    i = 0
    while i < blocks_len - k + 1:
        for index in indexes:
            if k + i > index >= i:
                temp_count += 1
        if temp_count < min_count:
            min_count = temp_count
        i += 1
        temp_count = 0

    return min_count


if __name__ == '__main__':
    assert(minimumRecolors(blocks="WWBBBWBBBBBWWBWWWB", k=16)) == 6
    assert(minimumRecolors(blocks="BWWWBB", k=6)) == 3
    assert (minimumRecolors(blocks="WBBWWBBWBW", k=7)) == 3
    assert (minimumRecolors(blocks="WBWBBBW", k=2)) == 0
    assert(minimumRecolors(blocks="WBBWWWWBBWWBBBBWWBBWWBBBWWBBBWWWBWBWW", k=15)) == 6
