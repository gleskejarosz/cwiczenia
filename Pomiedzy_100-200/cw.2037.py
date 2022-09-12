def minMovesToSeat(seats: list, students: list) -> int:
    moves = 0
    seats.sort()
    students.sort()

    for idx, seat in enumerate(seats):
        moves += abs(seat - students[idx])

    return moves


if __name__ == '__main__':
    assert (minMovesToSeat(seats=[3, 1, 5], students=[2, 7, 4])) == 4
    assert (minMovesToSeat([4, 1, 5, 9], students=[1, 3, 2, 6])) == 7
    assert (minMovesToSeat(seats=[2, 2, 6, 6], students=[1, 3, 2, 6])) == 4
