from lib.read_inputs import read_inputs

TEST_INPUT_PATH = "inputs/test_5.txt"
INPUT_PATH = "inputs/5.txt"

def part_1(path: str) -> int:
    score: int = 0
    text = read_inputs(path)
    ranges, ingredients = text.split("\n\n")
    ranges = [tuple(map(int, x.split("-"))) for x in ranges.splitlines()]
    ingredients = [int(x) for x in ingredients.splitlines()]
    for i in ingredients:
        for start, end in ranges:
            if start <= i <= end:
                score += 1
                break
    return score

def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    ranges.sort(key = lambda x: x[0])
    merged = list()
    for curr_range in ranges:
        if not merged or merged[-1][1] < curr_range[0]:
            merged.append(curr_range)
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], curr_range[1]))
    return merged

def part_2(path: str) -> int:
    score: int = 0
    fresh_ids = set()
    text = read_inputs(path)
    ranges, ingredients = text.split("\n\n")
    ranges = [tuple(map(int, x.split("-"))) for x in ranges.splitlines()]
    merged_ranges = merge_ranges(ranges)
    for start, end in merged_ranges:
        score += end - start + 1
    return score

def main() -> None:
    print(f"Part 1 score: {part_1(INPUT_PATH)}")
    print(f"Part 2 score: {part_2(INPUT_PATH)}")

if __name__ == "__main__":
    main()
