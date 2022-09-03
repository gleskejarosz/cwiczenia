def countVowelSubstrings(word: str) -> int:
    vowels = ['a', 'e', 'i', 'o', 'u']
    substrings = []
    substring = ""
    count = 0
    temp_count = 0

    for letter in word:
        if letter in vowels:
            substring += letter
        else:
            substrings.append(substring)
            substring = ""
    substrings.append(substring)

    for idx, substring in enumerate(substrings):
        if len(substring) < 5:
            substrings.pop(idx)

    for elem in substrings:
        i = 0
        j = len(elem)
        while i + 5 <= j:
            while i + 5 <= j:
                test_elem = elem[i: j]
                for vowel in vowels:
                    if vowel in test_elem:
                        temp_count += 1
                if temp_count == 5:
                    count += 1
                temp_count = 0
                i += 1
            i = 0
            j -= 1

    return count


if __name__ == '__main__':
    assert(countVowelSubstrings("aeiouu")) == 2
    assert(countVowelSubstrings("unicornarihan")) == 0
    assert(countVowelSubstrings("cuaieuouac")) == 7
