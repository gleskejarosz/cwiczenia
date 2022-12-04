def countBalls(lowLimit: int, highLimit: int) -> int:
    boxes = []
    balls = []

    for num in range(lowLimit, highLimit + 1):
        elem = str(num)
        temp_sum = 0
        for e in elem:
            temp_sum += int(e)
        if temp_sum in boxes:
            pos = boxes.index(temp_sum)
            balls[pos] += 1
        else:
            boxes.append(temp_sum)
            balls.append(1)

    return max(balls)


if __name__ == '__main__':
    assert (countBalls(lowLimit=1, highLimit=10)) == 2
    assert (countBalls(lowLimit=5, highLimit=15)) == 2
    assert (countBalls(lowLimit=19, highLimit=28)) == 2
