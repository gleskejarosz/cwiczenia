def halvesAreAlike(s: str) -> bool:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    s_list = list(s)

    s_half = int(len(s_list) / 2)
    a = s_list[0: s_half]
    b = s_list[s_half:]
    count_a = 0
    count_b = 0

    for vowel in a:
        if vowel in vowels:
            count_a += 1

    for vowel in b:
        if vowel in vowels:
            count_b += 1

    if count_a == count_b:
        return True
    else:
        return False


if __name__ == '__main__':
    assert(halvesAreAlike("book")) is True
    assert(halvesAreAlike("textbook")) is False
