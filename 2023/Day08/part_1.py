from aoc_utilities.input_handling import TxtInput


def parse_lines(lines):
    instruction_string = lines[0]
    instructions = [0 if letter == "L" else 1 for letter in instruction_string]
    maps = {}
    for item in lines[2:]:
        subitems = item.split(' ')
        origin = subitems[0]
        left = subitems[2][1:-1]
        right = subitems[3][:-1]
        maps[origin] = (left, right)
    return instructions, maps


def main(lines):
    steps = 0
    instructions, maps = parse_lines(lines)
    current_node = 'AAA'
    while current_node != 'ZZZ':
        for instruction in instructions:
            steps += 1
            current_node = maps[current_node][instruction]
    return steps


if __name__ == '__main__':
    lines = TxtInput('input.txt').lines
    print(f"Solution: {main(lines)}")
