def processQueries(queries: list, m: int) -> list:
    p = [x for x in range(m + 1) if x > 0]
    result = []

    for idx, query in enumerate(queries):
        pos = p.index(query)
        result.append(pos)
        p.pop(pos)
        p.insert(0, query)

    return result


if __name__ == '__main__':
    assert (processQueries(queries=[3, 1, 2, 1], m=5)) == [2, 1, 2, 1]
    assert (processQueries(queries=[4, 1, 2, 2], m=4)) == [3, 1, 2, 0]
    assert (processQueries(queries=[7, 5, 5, 8, 3], m=8)) == [6, 5, 0, 7, 5]
