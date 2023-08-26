from typing import List


def fullJustify(words: List[str], maxWidth: int) -> List[str]:
    result = []
    pre_lines = []
    line = []
    line_left = maxWidth
    idx = 0
    while idx < len(words):
        word = words[idx]
        word_len = len(word)
        if word_len <= line_left:
            line.append(word)
            line_left -= word_len + 1
        else:
            pre_lines.append(line)
            line_left = maxWidth
            line = []
            idx -= 1
            counter = 0
        idx += 1
    pre_lines.append(line)

    idx = 0
    while idx < len(pre_lines) - 1:
        old_line = pre_lines[idx]
        letters = 0
        for word in old_line:
            letters += len(word)
        word_count = len(old_line)
        spaces = maxWidth - letters
        if word_count - 1 > 0:
            spaces_per_word = spaces // (word_count - 1)
        else:
            spaces_per_word = 0
        left = spaces - (spaces_per_word * (word_count - 1))
        new_line = ""
        for word in old_line[:word_count - 1]:
            new_line += word + " " * spaces_per_word
            if left > 0:
                new_line += " "
                left -= 1
        new_line += old_line[word_count - 1]
        if word_count == 1:
            left = maxWidth - letters
            new_line += " " * left
        result.append(new_line)
        idx += 1

    last_line = pre_lines[-1:]
    new_line = ""
    for word in last_line[0]:
        new_line += word
        new_line += " "
    new_line = new_line.rstrip(" ")
    left = maxWidth - len(new_line)
    new_line += " " * left
    result.append(new_line)
    return result


if __name__ == '__main__':
    assert(fullJustify(
        words=["ask", "not", "what", "your", "country", "can", "do", "for", "you", "ask", "what", "you", "can", "do",
               "for", "your", "country"], maxWidth=16)) == ['ask   not   what', 'your country can', 'do  for  you ask',
                                                            'what  you can do', 'for your country']
    assert (fullJustify(words=["This", "is", "an", "example", "of", "text", "justification."], maxWidth=16)) == [
        "This    is    an",
        "example  of text",
        "justification.  "
    ]
    assert (fullJustify(words=["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth=16)) == [
        "What   must   be",
        "acknowledgment  ",
        "shall be        "
    ]
    assert (fullJustify(
        words=["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
               "Art", "is", "everything", "else", "we", "do"], maxWidth=20)) == [
               "Science  is  what we",
               "understand      well",
               "enough to explain to",
               "a  computer.  Art is",
               "everything  else  we",
               "do                  "
           ]
