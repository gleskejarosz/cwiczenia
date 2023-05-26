def numIslands(grid: list) -> int:
    max_row = len(grid)
    max_col = len(grid[0])
    islands = 0

    def land(row, col):
        if grid[row][col] == "1":
            grid[row][col] = "land"
            if col < max_col - 1:
                land(row, col + 1)
            if col > 0:
                land(row, col - 1)
            if row > 0:
                land(row - 1, col)
            if row < max_row - 1:
                land(row + 1, col)

    for row in range(max_row):
        for col in range(max_col):
            if grid[row][col] == "1":
                islands += 1
                land(row, col)

    return islands


if __name__ == '__main__':
    assert (numIslands(grid=[
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ])) == 1
    assert (numIslands(grid=[
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ])) == 3
