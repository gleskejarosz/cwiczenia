def minAddToMakeValid(s: str) -> int:
    counter = 0
    temp_counter = 0

    for elem in s:
        if elem == "(":
            counter += 1
        if elem == ")":
            if counter > 0:
                counter -= 1
            else:
                temp_counter += 1

    result = counter + temp_counter

    return result


if __name__ == '__main__':
    assert(minAddToMakeValid("())")) == 1
    assert(minAddToMakeValid("(((")) == 3
    assert(minAddToMakeValid("()))((")) == 4
