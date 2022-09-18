import string


def slowestKey(releaseTimes: list, keysPressed: str) -> str:
    alphabet = list(string.ascii_lowercase)
    number = [x for x in range(26)]
    alp_dict = {k: v for k, v in zip(alphabet, number)}
    value = 0
    letter = ""

    for idx, key in enumerate(keysPressed):
        if idx == 0:
            difference = releaseTimes[idx]
        else:
            difference = releaseTimes[idx] - releaseTimes[idx - 1]
        if difference == value:
            if alp_dict[key] > alp_dict[letter]:
                letter = key
        if difference > value:
            value = difference
            letter = key

    return letter


if __name__ == '__main__':
    assert (slowestKey(releaseTimes=[9, 29, 49, 50], keysPressed="cbcd")) == "c"
    assert (slowestKey(releaseTimes=[12, 23, 36, 46, 62], keysPressed="spuda")) == "a"
