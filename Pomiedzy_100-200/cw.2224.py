def convertTime(current: str, correct: str) -> int:
    current_min = int(current[:2]) * 60 + int(current[3:])
    correct_min = int(correct[:2]) * 60 + int(correct[3:])
    time_cal = correct_min - current_min
    counter = 0
    dividers = [60, 15, 5, 1]

    for divider in dividers:
        if time_cal == 0:
            break
        counter += time_cal // divider
        time_cal = time_cal % divider

    return counter


if __name__ == '__main__':
    assert (convertTime(current="02:30", correct="04:35")) == 3
    assert (convertTime(current="11:00", correct="11:01")) == 1
