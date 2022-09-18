def maxNumberOfBalloons(text: str) -> int:
    balloon_counter = {letter: text.count(letter) for letter in text}
    temp_counter = []
    if "b" in text:
        temp_counter.append(balloon_counter["b"])
    if "a" in text:
        temp_counter.append(balloon_counter["a"])
    if "n" in text:
        temp_counter.append(balloon_counter["n"])
    if "o" in text:
        temp_counter.append(balloon_counter["o"] // 2)
    if "l" in text:
        temp_counter.append(balloon_counter["l"] // 2)
    if len(temp_counter) != 5:
        return 0
    return min(temp_counter)


if __name__ == '__main__':
    assert(maxNumberOfBalloons("nlaebolko")) == 1
    assert(maxNumberOfBalloons("loonbalxballpoon")) == 2
    assert(maxNumberOfBalloons("leetcode")) == 0
