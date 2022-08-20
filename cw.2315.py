def countAsterisks(s: str) -> int:

    while s.find("|") >= 0:
        pos1 = s.find("|")
        pos2 = s[pos1 + 1: len(s)].find("|") + pos1 + 1
        s = s[0: pos1] + s[pos2 + 1: len(s)]

    return s.count("*")


if __name__ == '__main__':
    assert(countAsterisks("l|*e*et|c**o|*de|")) == 2
    assert(countAsterisks("iamprogrammer")) == 0
    assert(countAsterisks("yo|uar|e**|b|e***au|tifu|l")) == 5
