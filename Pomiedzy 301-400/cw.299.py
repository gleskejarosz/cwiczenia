def getHint(secret: str, guess: str) -> str:
    count_dict = {}

    for num in set(guess):
        qty = guess.count(num)
        if num in secret:
            q = secret.count(num)
            count_dict[num] = min(qty, q)

    bulls = 0
    cows = 0

    for elem in count_dict:
        for i, n in enumerate(guess):
            if elem == n:
                for idx, num in enumerate(secret):
                    if i == idx and elem == num:
                        bulls += 1
                        count_dict[elem] -= 1

    for value in count_dict.values():
        cows += value

    return str(bulls) + "A" + str(cows) + "B"


if __name__ == '__main__':
    assert(getHint(secret="1113", guess="0100")) == "1A0B"
    assert (getHint(secret="1807", guess="7810")) == "1A3B"
    assert (getHint(secret="1123", guess="0111")) == "1A1B"
