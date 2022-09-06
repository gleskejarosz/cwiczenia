def reformatNumber(number: str) -> str:
    for n in number:
        if n.isdigit() is False:
            number = number.replace(n, "")

    num_list = []
    temp_num = ""
    result = ""

    for elem in number:
        temp_num += elem
        if len(temp_num) == 3:
            num_list.append(temp_num)
            temp_num = ""

    if temp_num != "":
        num_list.append(temp_num)

    if len(num_list[-1]) == 1:
        last_4 = num_list[-2] + num_list[-1]
        num_list.pop(-1)
        num_list.pop(-1)
        num_list.append(last_4[:2])
        num_list.append(last_4[2:])

    for elem in num_list:
        result += elem + "-"

    return result.rstrip("-")


if __name__ == '__main__':
    assert(reformatNumber("1-23-45 6")) == "123-456"
    assert(reformatNumber("123 4-567")) == "123-45-67"
    assert(reformatNumber("123 4-5678")) == "123-456-78"
