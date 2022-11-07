def garbageCollection(garbage: list, travel: list) -> int:
    result = 0
    travel.append(0)
    last_g = 0
    last_p = 0
    last_m = 0

    for idx, elem in enumerate(garbage):
        if "G" in elem:
            last_g = idx
        if "P" in elem:
            last_p = idx
        if "M" in elem:
            last_m = idx

    for idx, elem in enumerate(garbage):
        if idx > last_g:
            result -= travel[idx - 1]
            break
        qty = elem.count("G")
        result += qty
        result += travel[idx]

    for idx, elem in enumerate(garbage):
        if idx > last_p:
            result -= travel[idx - 1]
            break
        qty = elem.count("P")
        result += qty
        result += travel[idx]

    for idx, elem in enumerate(garbage):
        if idx > last_m:
            result -= travel[idx - 1]
            break
        qty = elem.count("M")
        result += qty
        result += travel[idx]

    return result


if __name__ == '__main__':
    assert (garbageCollection(garbage=["G", "P", "GP", "GG"], travel=[2, 4, 3])) == 21
    assert (garbageCollection(garbage=["MMM", "PGM", "GP"], travel=[3, 10])) == 37
    assert (garbageCollection(garbage=["G", "M"], travel=[1]))
