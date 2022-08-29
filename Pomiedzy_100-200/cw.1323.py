def maximum69Number (num: int) -> int:
    num_list = list(str(num))

    for idx in range(len(num_list)):
        if num_list[idx] == "6":
            num_list[idx] = "9"
            break

    result = ""
    for n in num_list:
        result += n

    return int(result)


if __name__ == '__main__':
    assert(maximum69Number(9669)) == 9969
    assert(maximum69Number(9996)) == 9999
    assert(maximum69Number(9999)) == 9999
