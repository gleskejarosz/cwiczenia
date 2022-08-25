def canConstruct(ransomNote: str, magazine: str) -> bool:
    magazine_list = list(magazine)
    for letter in ransomNote:
        if letter not in magazine_list:
            return False
        magazine_list.remove(letter)
    return True


if __name__ == '__main__':
    assert (canConstruct(ransomNote="a", magazine="b")) is False
    assert (canConstruct(ransomNote="aa", magazine="ab")) is False
    assert (canConstruct(ransomNote="aa", magazine="aab")) is True
    assert(canConstruct(ransomNote="aab", magazine="baa")) is True
