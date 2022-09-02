def toGoatLatin(sentence: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u', "A", "E", "I", "O", "U"]
    sentence_list = sentence.split(" ")

    for idx, word in enumerate(sentence_list):
        if word[0] in vowels:
            sentence_list[idx] += "ma"
        else:
            letter = word[0]
            sentence_list[idx] = word[1:] + letter + "ma"

    for idx, word in enumerate(sentence_list):
        sentence_list[idx] += ("a" * (idx + 1))

    result = ""
    for elem in sentence_list:
        result += elem + " "

    return result.rstrip(" ")


if __name__ == '__main__':
    assert(toGoatLatin("I speak Goat Latin")) == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
    assert(toGoatLatin("The quick brown fox jumped over the lazy dog")) ==\
          "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
