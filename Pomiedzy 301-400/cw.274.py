def hIndex(citations: list) -> int:
    citations_len = len(citations)
    citations.sort(reverse=True)

    if citations_len == 1 and citations[0] > 0:
        return 1
    if citations[-1] >= citations_len:
        return citations_len
    for n in range(citations_len):
        if citations[n] < n + 1:
            return n
    return 0


if __name__ == '__main__':
    assert (hIndex(citations=[3, 0, 6, 1, 5])) == 3
    assert (hIndex(citations=[1, 3, 1])) == 1

