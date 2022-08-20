def truncateSentence(s: str, k: int) -> str:
    s_list = s.split(" ")
    s_list = s_list[0: k]

    result = ""
    for word in s_list:
        result += word
        result += " "

    return result.rstrip(" ")


if __name__ == '__main__':
    assert(truncateSentence(s="Hello how are you Contestant", k=4)) == "Hello how are you"
    assert(truncateSentence(s="What is the solution to this problem", k=4)) == "What is the solution"
    assert(truncateSentence(s="chopper is not a tanuki", k=5)) == "chopper is not a tanuki"
