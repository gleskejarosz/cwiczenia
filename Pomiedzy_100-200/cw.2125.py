def numberOfBeams(bank: list) -> int:
    counter = []
    laser_beams = 0
    prev_laser = 0

    if len(bank) == 1:
        return 0

    for beam in bank:
        qty = beam.count("1")
        if qty > 0:
            counter.append(qty)

    for laser in counter:
        laser_beams += prev_laser * laser
        prev_laser = laser

    return laser_beams


if __name__ == '__main__':
    assert (numberOfBeams(["011001", "000000", "010100", "001000"])) == 8
    assert (numberOfBeams(["000", "111", "000"])) == 0
