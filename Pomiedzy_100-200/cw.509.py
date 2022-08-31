def fib(n: int) -> int:
    fib_list = [0, 1, 1]

    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    for num in range(3, n):
        fib_elem = fib_list[-1] + fib_list[-2]
        fib_list.append(fib_elem)

    fib_sum = fib_list[-1] + fib_list[-2]
    return fib_sum


if __name__ == '__main__':
    assert(fib(2)) == 1
    assert(fib(3)) == 2
    assert(fib(4)) == 3
