def shortestCompletingWord(licensePlate: str, words: list) -> str:
    license_plate = licensePlate.lower()
    licence_dict = {k: license_plate.count(k) for k in license_plate}
    temp_count = 0
    result = {0: ""}

    for word in words:
        temp_len = len(word)
        for letter in set(word):
            if letter in licence_dict:
                qty = licence_dict[letter]
                qty_in_word = word.count(letter)
                if qty >= qty_in_word:
                    temp_count += qty_in_word
                else:
                    temp_count += qty
        prev_count = max(result.keys())
        prev_len = len(result[prev_count])
        if prev_count == temp_count and temp_count > 0:
            if prev_len > temp_len:
                result[temp_count] = word
        if prev_count < temp_count:
            result[temp_count] = word
        temp_count = 0

    max_count = max(result.keys())
    return result[max_count]


if __name__ == '__main__':
    assert (shortestCompletingWord(licensePlate="1s3 PSt", words=["step", "steps", "stripe", "stepple"])) == "steps"
    assert (shortestCompletingWord(licensePlate="1s3 456", words=["looks", "pest", "stew", "show"])) == "pest"
    assert (shortestCompletingWord(licensePlate="Ah71752",
                                   words=["suggest", "letter", "of", "husband", "easy", "education", "drug", "prevent",
                                          "writer", "old"])) == "husband"
    assert (shortestCompletingWord(licensePlate="OgEu755",
                                   words=["enough", "these", "play", "wide", "wonder", "box", "arrive", "money", "tax",
                                          "thus"])) == "enough"
    assert (shortestCompletingWord(licensePlate="GAn3936",
                                   words=["picture", "community", "stuff", "above", "be", "around", "can", "father",
                                          "avoid", "agent"])) == "agent"
