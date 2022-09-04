def minPartitions(n: str) -> int:
    n_list = [int(x) for x in n]

    return max(n_list)


def minPartitions2(n: str) -> int:
    num = int(n)

    counter = 0

    while num > 0:
        deci_binary = ""
        for elem in str(num):
            if int(elem) >= 1:
                deci_binary += str(1)
            else:
                deci_binary += str(0)
        num = num - int(deci_binary)
        counter += 1

    return counter


if __name__ == '__main__':
    assert(minPartitions("32")) == 3
    assert(minPartitions("82734")) == 8
    assert(minPartitions("27346209830709182346")) == 9
    assert(minPartitions2("32")) == 3
    assert(minPartitions2("82734")) == 8
    assert(minPartitions2("27346209830709182346")) == 9
