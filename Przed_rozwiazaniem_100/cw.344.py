def reverseString(s: list):
    """
    Do not return anything, modify s in-place instead.
    """
    s.reverse()


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    reverseString(s)
    assert s == ["o", "l", "l", "e", "h"]
