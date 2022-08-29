def mergeSimilarItems(items1: list, items2: list) -> list:
    result = []
    items_dict = dict(items1)

    for item in items2:
        if item[0] in items_dict:
            items_dict[item[0]] += item[1]
        else:
            items_dict[item[0]] = item[1]

    for elem in items_dict:
        result.append([elem, items_dict[elem]])

    return sorted(result)


if __name__ == '__main__':
    assert (mergeSimilarItems(items1=[[1, 1], [4, 5], [3, 8]], items2=[[3, 1], [1, 5]])) == [[1, 6], [3, 9], [4, 5]]
    assert (mergeSimilarItems(items1=[[1, 1], [3, 2], [2, 3]], items2=[[2, 1], [3, 2], [1, 3]])) == [[1, 4], [2, 4],
                                                                                                     [3, 4]]
    assert (mergeSimilarItems(items1=[[1, 3], [2, 2]], items2=[[7, 1], [2, 2], [1, 4]])) == [[1, 7], [2, 4], [7, 1]]
