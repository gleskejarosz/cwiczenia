def strongPasswordCheckerII(password: str) -> bool:
    special_char = "!@#$%^&*()-+"
    special_chars = 0
    lower_char = 0
    upper_char = 0
    digits = 0
    len_password = len(password)

    if len_password < 8:
        return False

    for idx, character in enumerate(password):
        if character.islower():
            lower_char += 1
        if character.isupper():
            upper_char += 1
        if character.isdigit():
            digits += 1
        if character in special_char:
            special_chars += 1
        if idx + 1 < len_password:
            if character == password[idx + 1]:
                return False

    if special_chars == 0:
        return False

    if lower_char == 0:
        return False

    if upper_char == 0:
        return False

    if digits == 0:
        return False

    return True


if __name__ == '__main__':
    assert(strongPasswordCheckerII("IloveLe3tcode!")) is True
    assert(strongPasswordCheckerII("Me+You--IsMyDream")) is False
    assert(strongPasswordCheckerII("1aB!")) is False
