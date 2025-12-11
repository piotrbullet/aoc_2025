from lib.read_inputs import read_inputs

INPUT_FILE = "inputs/3.txt"

def part_1() -> int:
    output_joltage: int = 0
    banks = read_inputs(INPUT_FILE).strip().splitlines()
    banks = [[int(i) for i in bank] for bank in banks]
    for b in banks:
        max_cell = max(b[:len(b)-1])
        for i, cell in enumerate(b):
            if cell == max_cell:
                second_cell = max(b[i+1:])
                output_joltage += int(str(cell)+str(second_cell))
                break
    return output_joltage
  
def find_max_val(l: list) -> tuple[int, str]:
    index, max_val = -1, -1
    for i, val in enumerate(l):
        if val > max_val:
            index, max_val = i, val
    return index, str(max_val)
 
def part_2() -> int:
    output_joltage: int = 0
    banks = read_inputs(INPUT_FILE).strip().splitlines()
    banks = [[int(i) for i in bank] for bank in banks]
    for b in banks:
        curr_ind = 0
        curr_numb_str = ""
        for i in reversed(list(range(0, 12))):
            ind, n = find_max_val(b[curr_ind:len(b)-i])
            curr_numb_str += n
            curr_ind += ind+1
        
        output_joltage += int(curr_numb_str)
        
    return output_joltage

def main() -> None:
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
    
if __name__ == "__main__":
    main()
    