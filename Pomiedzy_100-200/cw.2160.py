def minimumSum(num: int) -> int:
    num_list = sorted(list(str(num)))

    sum1 = int(num_list[0] + num_list[2]) + int(num_list[1] + num_list[3])
    sum2 = int(num_list[0] + num_list[3]) + int(num_list[1] + num_list[2])

    return min(sum1, sum2)


if __name__ == '__main__':
    assert(minimumSum(2932)) == 52
    assert(minimumSum(4009)) == 13
