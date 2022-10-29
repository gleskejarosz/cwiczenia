def countTime(time: str) -> int:
    hours = [x for x in range(24)]
    minutes = [x for x in range(60)]
    counter_t = 0
    counter_i = 0
    counter_m = 0
    counter_e = 0

    if time.count("?") == 0:
        return 1

    if time[0] == "?" and time[1] == "?":
        counter_t = 24

    if time[3] == "?" and time[4] == "?":
        counter_m = 60

    if time[0] == "?" and time[1] != "?":
        for num in range(3):
            time_new = int(str(num) + time[1])
            t = hours.count(time_new)
            if t <= 24:
                counter_t += t

    if time[1] == "?" and time[0] != "?":
        for num in range(10):
            if time[0] == "0":
                time_new = num
            else:
                time_new = int(time[0] + str(num))
            i = hours.count(time_new)
            counter_i += i

    if time[3] == "?" and time[4] != "?":
        for num in range(6):
            time_new = int(str(num) + time[4])
            m = minutes.count(time_new)
            counter_m += m

    if time[4] == "?" and time[3] != "?":
        for num in range(10):
            if time[3] == "0":
                time_new = num
            else:
                time_new = int(time[3] + str(num))
            e = minutes.count(time_new)
            counter_e += e

    if counter_t + counter_i > 0:
        if counter_m + counter_e > 0:
            counter = (counter_t + counter_i) * (counter_m + counter_e)
        else:
            counter = counter_t + counter_i
    else:
        counter = counter_m + counter_e

    return counter


if __name__ == '__main__':
    assert(countTime("?5:00")) == 2
    assert(countTime("0?:0?")) == 100
    assert(countTime("??:??")) == 1440
    assert(countTime("0?:5?")) == 100
    assert(countTime("21:08")) == 1
    