def sortSentence(s: str) -> str:
    s_list = s.split(" ")
    sentence = []
    result = ""
    for num in range(1, len(s_list) + 1):
        sentence.append(num)
    for elem in s_list:
        last_elem = elem[:-2:-1]
        i = int(last_elem) - 1
        elem = elem.rstrip(last_elem)
        sentence[i] = elem
    for word in sentence:
        result += word
        result += " "
    return result.rstrip(" ")


if __name__ == '__main__':
    assert(sortSentence("is2 sentence4 This1 a3")) == "This is a sentence"
    assert(sortSentence("Myself2 Me1 I4 and3")) == "Me Myself and I"
