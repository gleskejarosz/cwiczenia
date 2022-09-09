def findOcurrences(text: str, first: str, second: str) -> list:
    text_list = text.split()
    result = []
    list_len = len(text_list)

    for idx, word in enumerate(text_list):
        if word == first and idx + 1 < list_len:
            if text_list[idx + 1] == second and idx + 2 < list_len:
                result.append(text_list[idx + 2])

    return result


if __name__ == '__main__':
    assert (findOcurrences(text="alice is a good girl she is a good student", first="a", second="good")) == ["girl",
                                                                                                             "student"]
    assert (findOcurrences(text="we will we will rock you", first="we", second="will")) == ["we", "rock"]
