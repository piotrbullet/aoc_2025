from lib.read_inputs import read_inputs

INPUT_PATH = r"inputs/1.txt"

def part_1():
    score = 0
    position = 50
    input_raw = read_inputs(INPUT_PATH)
    safe_inputs = [(l[0], int(l[1:])) for l in input_raw.splitlines()]

    for direction, dist in safe_inputs:
        if direction == "R":
            position += dist
        else:
            position -= dist
        
        if position % 100 == 0:
            score += 1
            
    return(score)

DIR_DICT = {"R": 1, "L": -1}

def part_2():
    score = 0
    position = 50
    prev_rotation = position // 100
    input_raw = read_inputs(INPUT_PATH)
    safe_inputs = [(l[0], int(l[1:])) for l in input_raw.splitlines()]

    for direction, dist in safe_inputs:
        score += dist // 100
        dist = dist % 100
        for x in range(dist):
            position += DIR_DICT[direction]
            position = position % 100
            if position == 0:
                score += 1
        
    return(score)

def main():
    score_part_1 = part_1()
    score_part_2 = part_2()
    print(f"Part 1: {score_part_1}")
    print(f"Part 2: {score_part_2}")

if __name__ == "__main__":
    main()