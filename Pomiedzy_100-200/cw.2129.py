def capitalizeTitle(title: str) -> str:
    title_list = title.split()
    result = ""

    for word in title_list:
        if len(word) < 3:
            result += word.lower()
            result += " "
        else:
            lower_letters = word.lower()
            first_letter = (word[0]).upper()
            new_word = first_letter + lower_letters[1:]
            result += new_word + " "

    return result.rstrip()


if __name__ == '__main__':
    assert(capitalizeTitle("capiTalIze tHe titLe")) == "Capitalize The Title"
    assert(capitalizeTitle("First leTTeR of EACH Word")) == "First Letter of Each Word"
    assert(capitalizeTitle("i lOve leetcode")) == "i Love Leetcode"
