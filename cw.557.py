def reverseWords(s: str) -> str:
    s_list = s.split(" ")
    result = ""
    temp_word = []

    for word in s_list:
        for letter in word:
            temp_word.insert(0, letter)
        for letter in temp_word:
            result += str(letter)
        result += " "
        temp_word = []

    return result.rstrip(" ")


if __name__ == '__main__':
    assert(reverseWords("Let's take LeetCode contest")) == "s'teL ekat edoCteeL tsetnoc"
    assert(reverseWords("God Ding")) == "doG gniD"
