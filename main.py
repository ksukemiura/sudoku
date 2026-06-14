grid = [[-1 for j in range(9)] for i in range(9)]


def main():
    for solution in get_solutions():
        print(solution)


def get_solutions(index=0):
    if index < 9 ** 2:
        row = index // 9
        col = index % 9
        for num in range(1, 10):
            if is_valid(row, col, num):
                grid[row][col] = num
                yield from get_solutions(index + 1)
                grid[row][col] = -1
    else:
        yield grid



def is_valid(row, col, num):
    if num in get_row(row):
        return False

    if num in get_col(col):
        return False

    box = (row // 3) * 3 + col // 3
    if num in get_box(box):
        return False

    return True


def get_row(row):
    return [grid[row][col] for col in range(9)]


def get_col(col):
    return [grid[row][col] for row in range(9)]


def get_box(box):
    r = (box // 3) * 3
    c = (box % 3) * 3
    return [grid[row][col] for row in range(r, r + 3) for col in range(c, c + 3)]


if __name__ == "__main__":
    main()
