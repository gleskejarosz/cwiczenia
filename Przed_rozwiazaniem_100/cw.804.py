import string


def uniqueMorseRepresentations(words) -> int:
    alphabet = list(string.ascii_lowercase)
    morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
             ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    morse_rep = {k: v for (k, v) in zip(alphabet, morse)}

    morse_words = []
    morse_word = ""
    for word in words:
        for letter in word:
            morse_l = morse_rep[letter]
            morse_word += morse_l
        morse_words.append(morse_word)
        morse_word = ""

    count = 0
    unique_morse_words = []
    for word in morse_words:
        if word not in unique_morse_words:
            unique_morse_words.append(word)
            count += 1

    return count


if __name__ == '__main__':
    assert (uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])) == 2
    assert (uniqueMorseRepresentations(["a"])) == 1
