def groupThePeople(groupSizes: list) -> list:
    result = []
    group = []

    for idx, group_size in enumerate(groupSizes):
        if group_size in group:
            pos = group.index(group_size)
            elem = result[pos]
            if len(elem) < group_size - 1:
                elem.append(idx)
            elif len(elem) == group_size - 1:
                elem.append(idx)
                group[pos] = "Full"
            else:
                result.append([idx])
                group.append(group_size)
        else:
            group.append(group_size)
            result.append([idx])

    return result


if __name__ == '__main__':
    assert (groupThePeople([3, 3, 3, 3, 3, 1, 3])) == [[0, 1, 2], [3, 4, 6], [5]]
    assert (groupThePeople([2, 1, 3, 3, 3, 2])) == [[0, 5], [1], [2, 3, 4]]
