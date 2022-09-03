def areNumbersAscending(s: str) -> bool:
    numbers = []
    list_s = s.split(" ")

    for elem in list_s:
        if elem.isdigit():
            numbers.append(elem)

    num_len = len(numbers)
    for idx, num in enumerate(numbers):
        if idx == num_len - 1:
            break
        if int(num) >= int(numbers[idx + 1]):
            return False

    return True


if __name__ == '__main__':
    assert (areNumbersAscending(s="1 box has 3 blue 4 red 6 green and 12 yellow marbles")) is True
    assert (areNumbersAscending(s="hello world 5 x 5")) is False
    assert (areNumbersAscending(s="sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s")) is False
