def fizzBuzz(n: int) -> list:
    result = []
    appended = 0
    for i in range(1, n + 1):
        if i % 15 == 0:
            if appended == 0:
                result.append("FizzBuzz")
                appended = 1
        if i % 3 == 0:
            if appended == 0:
                result.append("Fizz")
                appended = 1
        if i % 5 == 0:
            if appended == 0:
                result.append("Buzz")
                appended = 1
        if appended == 0:
            result.append(str(i))
        appended = 0

    return result


if __name__ == '__main__':
    assert (fizzBuzz(3)) == ["1", "2", "Fizz"]
    assert (fizzBuzz(5)) == ["1", "2", "Fizz", "4", "Buzz"]
    assert (fizzBuzz(15)) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14",
                              "FizzBuzz"]
    