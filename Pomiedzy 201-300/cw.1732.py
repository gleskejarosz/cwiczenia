def largestAltitude(gain: list) -> int:
    altitudes = [0]

    for idx, g in enumerate(gain):
        g_new = altitudes[idx] + g
        altitudes.append(g_new)

    return max(altitudes)


if __name__ == '__main__':
    assert (largestAltitude([-5, 1, 5, 0, -7])) == 1
    assert (largestAltitude([-4, -3, -2, -1, 4, 3, 2])) == 0
