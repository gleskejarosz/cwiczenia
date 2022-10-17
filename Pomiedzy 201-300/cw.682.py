from functools import reduce


def calPoints(operations: list) -> int:
    sum_of_all_scores = []

    for operation in operations:
        operation_len = len(sum_of_all_scores)
        if operation == "+":
            value = sum_of_all_scores[operation_len - 1] + sum_of_all_scores[operation_len - 2]
            sum_of_all_scores.append(value)
        if operation == "D":
            value = sum_of_all_scores[operation_len - 1] * 2
            sum_of_all_scores.append(value)
        if operation == "C":
            sum_of_all_scores = sum_of_all_scores[:-1]
        if operation != "+" and operation != "D" and operation != "C":
            sum_of_all_scores.append(int(operation))

    if len(sum_of_all_scores) == 0:
        return 0

    result = reduce(lambda x, total: total + x, sum_of_all_scores)
    return result


if __name__ == '__main__':
    assert (calPoints(["5", "2", "C", "D", "+"])) == 30
    assert (calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"])) == 27
    assert (calPoints(["1", "C"])) == 0
