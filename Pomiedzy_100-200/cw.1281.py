from functools import reduce


def subtractProductAndSum(n: int) -> int:
    n_list = list(str(n))
    int_list = [eval(i) for i in n_list]

    mlp_n = reduce(lambda total, item: total * item, int_list)
    sum_n = reduce(lambda total, item: total + item, int_list)

    return mlp_n - sum_n


if __name__ == '__main__':
    assert (subtractProductAndSum(234)) == 15
    assert (subtractProductAndSum(4421)) == 21
