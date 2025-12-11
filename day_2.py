from lib.read_inputs import read_inputs

INPUT_PATH = "inputs/2.txt"

def part_1() -> int:
    score: int = 0
    text = read_inputs(INPUT_PATH).strip()
    ids = text.split(",")
    for i in ids:
        x, y = i.split("-")
        if len(x)%2 and len(y)%2:
            continue
        if len(x)%2:
            x = "1" + "0"*len(x)
        if len(y)%2:
            y = "9" * (len(y)-1)
        invalids = [x for x in range(int(x), int(y)+1) if str(x)[:len(str(x))//2] == str(x)[len(str(x))//2:]]
        score += sum(invalids)
    return score

def part_2() -> int:
    score: int = 0
    ids = read_inputs(INPUT_PATH).strip().split(",")
    max_val = max([int(x.split("-")[-1]) for x in ids])
    max_repeat = len(str(max_val))
    poss_repeats = [x for x in range(2, max_repeat+1)]
    max_rang = int("9"*(max_repeat//2))
    candidates = set()
    for i in range(1, max_rang):
        for j in poss_repeats:
            poss_cand = int(str(i)*j)
            if poss_cand > max_val:
                break
            candidates.add(poss_cand)
            
    candidates = list(candidates)
    ids = [map(int, i.split("-")) for i in ids]
    for x, y in ids:
        for c in candidates:
            if x <= c <= y:
                score += c
    return score

def main():
    print(f"Part 1 answer: {part_1()}")
    print(f"Part 2 answer: {part_2()}")
    
if __name__ == "__main__":
    main()