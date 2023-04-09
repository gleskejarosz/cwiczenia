def average(salary: list) -> float:
    salary.remove(min(salary))
    salary.remove((max(salary)))

    counter = 0
    salary_sum = 0

    for payment in salary:
        counter += 1
        salary_sum += payment

    avg = salary_sum / counter

    return avg


if __name__ == '__main__':
    assert (average([4000, 3000, 1000, 2000])) == 2500
    assert (average([1000, 2000, 3000])) == 2000
