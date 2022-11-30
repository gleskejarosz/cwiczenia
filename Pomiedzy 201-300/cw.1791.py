def findCenter(edges: list) -> int:
    edges_len = len(edges)
    nums = []
    for elem in edges:
        for num in elem:
            nums.append(num)

    for num in nums:
        if nums.count(num) == edges_len:
            return num


if __name__ == '__main__':
    assert (findCenter([[1, 2], [2, 3], [4, 2]])) == 2
    assert (findCenter([[1, 2], [5, 1], [1, 3], [1, 4]])) == 1
