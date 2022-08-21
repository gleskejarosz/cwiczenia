def countPoints(rings: str) -> int:
    rings_list = list(rings)
    count = 0
    checked = ""
    if len(rings) < 6:
        return 0
    for n in range(0, 10):
        while str(n) in rings_list:
            pos = rings_list.index(str(n))
            if pos >= 0:
                if rings_list[pos - 1] == "R":
                    checked += "R"
                if rings_list[pos - 1] == "G":
                    checked += "G"
                if rings_list[pos - 1] == "B":
                    checked += "B"
            rings_list.pop(pos)
            rings_list.pop(pos - 1)
            if "R" in checked and "G" in checked and "B" in checked:
                count += 1
                break
        checked = ""
    else:
        return count


if __name__ == '__main__':
    assert(countPoints("B0B6G0R6R0R6G9")) == 1
    assert(countPoints("B0R0G0R9R0B0G0")) == 1
    assert(countPoints("G4")) == 0
