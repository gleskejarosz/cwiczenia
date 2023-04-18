class NumArray:

    def __init__(self, nums: list):
        self.A = nums

    def sumRange(self, left: int, right: int) -> int:
        sum_range = 0
        for num in self.A[left: right + 1]:
            sum_range += num
        return sum_range


if __name__ == '__main__':
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    assert(obj.sumRange(0, 2)) == 1
    assert (obj.sumRange(2, 5)) == -1
    assert (obj.sumRange(0, 5)) == -3
