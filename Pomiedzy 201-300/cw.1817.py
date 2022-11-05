def findingUsersActiveMinutes(logs: list, k: int) -> list:
    result = [0 for x in range(k)]
    users = []
    users_minutes = []

    for log in logs:
        user = log[0]
        if user not in users:
            users.append(user)
            users_minutes.append(set())
            users_minutes[-1].add(log[1])
        else:
            pos = list(users).index(user)
            users_minutes[pos].add(log[1])

    for idx, elem in enumerate(users_minutes):
        uam = len(elem)
        result[uam - 1] += 1

    return result


if __name__ == '__main__':
    assert (findingUsersActiveMinutes(logs=[[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]], k=5)) == [0, 2, 0, 0, 0]
    assert (findingUsersActiveMinutes(logs=[[1, 1], [2, 2], [2, 3]], k=4)) == [1, 1, 0, 0]
    assert (findingUsersActiveMinutes(logs=
                                      [[305589003, 4136], [305589004, 4139], [305589004, 4141], [305589004, 4137],
                                       [305589001, 4139], [305589001, 4139]], k=6)) == [2, 0, 1, 0, 0, 0]
