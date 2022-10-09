def removeOuterParentheses(s: str) -> str:
    result = ""
    strings = []
    string = ""
    open_bracket = "("
    open_count = 0
    close_bracket = ")"
    close_count = 0

    for idx, elem in enumerate(s):
        if elem == open_bracket:
            string += elem
            open_count += 1
        if elem == close_bracket:
            string += elem
            close_count += 1
        if open_count - close_count == 0:
            strings.append(string)
            string = ""

    for elem in strings:
        result += elem[1:-1]

    return result


if __name__ == '__main__':
    assert (removeOuterParentheses("(()())(())")) == "()()()"
    assert (removeOuterParentheses("(()())(())(()(()))")) == "()()()()(())"
    assert (removeOuterParentheses("()()")) == ""
