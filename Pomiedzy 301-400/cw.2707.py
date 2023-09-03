def minExtraChar(s: str, dictionary: list) -> int:
    dictionary.sort(key=len, reverse=True)
    my_dict = {}

    def dfs(text):
        if len(text) <= 0:
            return 0

        if len(text) in my_dict:
            return my_dict[len(text)]

        min_char = len(text)

        for word in dictionary:
            if text == word:
                min_char = 0
                my_dict[len(text)] = min_char
                return min_char

            elif text[:len(word)] == word:
                result = dfs(text[len(word):])
                min_char = min(min_char, result)

        min_char = min(min_char, 1 + dfs(text[1:]))

        my_dict[len(text)] = min_char

        return min_char

    return dfs(s)


if __name__ == '__main__':
    assert (minExtraChar(s="azvzulhlwxwobowijiyebeaskecvtjqwkmaqnvnaomaqnvf",
                         dictionary=["na", "i", "edd", "wobow", "kecv", "b", "n", "or", "jj", "zul", "vk", "yeb",
                                     "qnfac", "azv", "grtjba", "yswmjn", "xowio", "u", "xi", "pcmatm", "maqnv"])) == 15
    assert (minExtraChar(s="leetscode", dictionary=["leet", "code", "leetcode"])) == 1
    assert (minExtraChar(s="sayhelloworld", dictionary=["hello", "world"])) == 3
