def sortPeople(names: list, heights: list) -> list:
    name_dict = {k: v for k, v in zip(heights, names)}
    heights_sorted = sorted(heights, reverse=True)
    result = []

    for height in heights_sorted:
        result.append(name_dict[height])

    return result


if __name__ == '__main__':
    assert (sortPeople(names=["Mary", "John", "Emma"], heights=[180, 165, 170])) == ["Mary", "Emma", "John"]
    assert (sortPeople(names=["Alice", "Bob", "Bob"], heights=[155, 185, 150])) == ["Bob", "Alice", "Bob"]
