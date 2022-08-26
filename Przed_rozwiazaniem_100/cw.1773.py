def countMatches(items, ruleKey, ruleValue):
    count = 0
    if ruleKey == "type":
        for elem in items:
            if elem[0] == ruleValue:
                count += 1
    if ruleKey == "color":
        for elem in items:
            if elem[1] == ruleValue:
                count += 1
    if ruleKey == "name":
        for elem in items:
            if elem[2] == ruleValue:
                count += 1
    return count


if __name__ == '__main__':
    assert (countMatches(
        items=[["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]],
        ruleKey="color", ruleValue="silver")) == 1
    assert (
        countMatches(items=[["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]],
                     ruleKey="type", ruleValue="phone")) == 2
