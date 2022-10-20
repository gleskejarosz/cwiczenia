def busyStudent(startTime: list, endTime: list, queryTime: int) -> int:
    counter = 0

    for idx, s in enumerate(startTime):
        homework_start = s
        homework_end = endTime[idx]
        for hour in range(homework_start, homework_end + 1):
            if hour == queryTime:
                counter += 1
                break

    return counter


if __name__ == '__main__':
    assert (busyStudent(startTime=[1, 2, 3], endTime=[3, 2, 7], queryTime=4)) == 1
    assert (busyStudent(startTime=[4], endTime=[4], queryTime=4)) == 1
