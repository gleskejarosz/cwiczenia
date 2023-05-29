def decodeString(s: str) -> str:
    substrings = []
    times = []
    repeat = 0
    result = ''

    for char in s:
        if char.isnumeric():
            repeat = repeat * 10 + int(char)
        elif char == '[':
            substrings.append(result)
            times.append(repeat)
            result = ''
            repeat = 0
        elif char == ']':
            freq = times.pop()
            prev = substrings.pop()
            result = prev + freq * result
        else:
            result += char
    return result


if __name__ == '__main__':
    assert(decodeString("3[a]2[bc]")) == "aaabcbc"
    assert(decodeString("3[a2[c]]")) == "accaccacc"
    assert(decodeString("2[abc]3[cd]ef")) == "abcabccdcdcdef"
