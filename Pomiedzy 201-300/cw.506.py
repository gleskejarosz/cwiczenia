def findRelativeRanks(score: list) -> list:
    result = []
    places = []
    sorted_score = sorted(score, reverse=True)

    for s in score:
        pos = sorted_score.index(s)
        places.append(pos + 1)

    for place in places:
        if place == 1:
            result.append("Gold Medal")
        if place == 2:
            result.append("Silver Medal")
        if place == 3:
            result.append("Bronze Medal")
        if place > 3:
            result.append(str(place))

    return result


if __name__ == '__main__':
    assert (findRelativeRanks([5, 4, 3, 2, 1])) == ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
    assert (findRelativeRanks([10, 3, 8, 9, 4])) == ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
