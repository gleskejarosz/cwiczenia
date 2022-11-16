def combinationSum(candidates: list, target: int) -> list:
    result = []

    def target_sum(idx, current_test, total):
        if total == target:
            result.append(current_test.copy())
            return
        if idx >= len(candidates) or total > target:
            return

        current_test.append(candidates[idx])
        target_sum(idx, current_test, total + candidates[idx])

        current_test.pop()
        target_sum(idx + 1, current_test, total)

    target_sum(0, [], 0)
    return result


if __name__ == '__main__':
    assert (combinationSum(candidates=[2, 3, 6, 7], target=7)) == [[2, 2, 3], [7]]
    assert (combinationSum(candidates=[2, 3, 5], target=8)) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert (combinationSum(candidates=[2], target=1)) == []
