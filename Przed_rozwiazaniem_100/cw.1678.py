def interpret(command):
    result = ""

    while len(command) > 0:
        if command[0] == "G":
            result += "G"
            command = command[1: len(command)]
        if command[0: 2] == "()":
            result += "o"
            command = command[2: len(command)]
        if command[0: 4] == "(al)":
            result += "al"
            command = command[4: len(command)]

    return result


if __name__ == '__main__':
    assert(interpret("G()(al)")) == "Goal"
    assert(interpret("G()()()()(al)")) == "Gooooal"
    assert(interpret("(al)G(al)()()G")) == "alGalooG"
    assert (interpret("GGG")) == "GGG"
