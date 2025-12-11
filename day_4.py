from lib.read_inputs import read_inputs
import numpy as np

TEST_INPUT_PATH = "inputs/test_4.txt"
INPUT_PATH = "inputs/4.txt"

ADJACENTS = ((-1, -1), (-1 , 0), (-1, 1), (0, 1), 
             (1, 1), (1, 0), (1, -1), (0, -1))

def valid_coordinate(x, y, X, Y):
    if 0 <= x <= X and 0 <= y <= Y:
        return True
    return False

def part_1(path: str) -> int:
    text = read_inputs(path).replace(".", "0").replace("@", "1")
    grid = [[int(val) for val in line] for line in text.splitlines()]
    score_grid = [[0 if x else 9 for x in y] for y in grid]
    Ylen = len(grid)-1
    Xlen = len(grid[0])-1
    for iy, y in enumerate(grid):
        for ix, x in enumerate(y):
            if not x:
                continue
            for dx, dy in ADJACENTS:
                nx, ny = ix+dx, iy+dy
                if valid_coordinate(nx, ny, Xlen, Ylen):
                    score_grid[ny][nx] += x
    arr = [[x < 4 for x in y] for y in score_grid]
    flat_score_array = [x for y in score_grid for x in y]
    
    return sum([x<4 for x in flat_score_array])

def remove_rolls(grid: np.array, removed_rolls: int) -> int:
    curr_removed = 0
    score_grid = np.array([[0 if x else 9 for x in y] for y in grid])
    for iy, y in enumerate(grid):
        for ix, x in enumerate(y):
            if not x:
                continue
            for dx, dy in ADJACENTS:
                nx, ny = ix+dx, iy+dy
                if 0 <= nx < grid.shape[1] and 0 <= ny < grid.shape[0]:
                    score_grid[ny][nx] += x
    rm_grid = score_grid < 4
    curr_removed = np.sum(rm_grid)

    if curr_removed:
        removed_rolls += curr_removed
        grid[score_grid < 4] = 0
        return remove_rolls(grid, removed_rolls)
    else:
        return removed_rolls

def part_2(path: str) -> int:
    text = read_inputs(path).replace(".", "0").replace("@", "1")
    grid = [[int(val) for val in line] for line in text.splitlines()]
    grid = np.array(grid)
    score = remove_rolls(grid, 0)
    return score

def main() -> None:
    print(f"Part 1 score: {part_1(INPUT_PATH)}")
    print(f"Part 2 score: {part_2(INPUT_PATH)}")

if __name__ == "__main__":
    main()