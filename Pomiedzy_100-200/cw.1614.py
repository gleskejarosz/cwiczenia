def maxDepth(s: str) -> int:
    start = 0
    depth = []

    for elem in s:
        if elem == "(":
            start += 1
        if elem == ")":
            depth.append(start)
            start -= 1

    if not depth:
        return 0
    else:
        return max(depth)


if __name__ == '__main__':
    assert(maxDepth("(1+(2*3)+((8)/4))+1")) == 3
    assert (maxDepth("(1)+((2))+(((3)))")) == 3
    assert(maxDepth("1")) == 0
