def destCity(paths: list) -> str:
    if len(paths) == 1:
        return paths[0][1]

    city_count = {}
    result = []

    for elem in paths:
        for city in elem:
            if city in city_count:
                city_count[city] += 1
            else:
                city_count[city] = 1

    for key, val in city_count.items():
        if val == 1:
            result.append(key)

    for elem in paths:
        for city in result:
            if elem[1] == city:
                return city


if __name__ == '__main__':
    assert (destCity([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]])) == "Sao Paulo"
    assert (destCity([["B", "C"], ["D", "B"], ["C", "A"]])) == "A"
    assert (destCity([["A", "Z"]])) == "Z"
    assert (destCity([["pYyNGfBYbm", "wxAscRuzOl"], ["kzwEQHfwce", "pYyNGfBYbm"]])) == "wxAscRuzOl"
