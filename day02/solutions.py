def parse_input(input):
    return [int(x) for x in input.split(',')]

def run_prog(ins):
    ins = ins.copy()
    ins_pointer = 0

    while ins_pointer < len(ins):
        op_code = ins[ins_pointer]

        if op_code == 1:
            v1, v2, v3 = ins[ins_pointer+1:ins_pointer+4]
            ins[v3] = ins[v1] + ins[v2]
            ins_pointer += 4
        elif op_code == 2:
            v1, v2, v3 = ins[ins_pointer+1:ins_pointer+4]
            ins[v3] = ins[v1] * ins[v2]
            ins_pointer += 4
        elif op_code == 99:
            break

    return ins

def day2_part1(input):
    ins = parse_input(input)

    ins[1] = 12
    ins[2] = 2
    ins = run_prog(ins)

    return ins[0]

def day2_part2(input):
    ins = parse_input(input)

    for x in range(100):
        for y in range(100):
            cpy = ins.copy()
            cpy[1] = x
            cpy[2] = y
            cpy = run_prog(cpy)
            if cpy[0] == 19690720:
                return 100 * x + y

    return None

if __name__ == "__main__":
    test_input = open('input.txt', 'r').read()

    print(day2_part1(test_input))

    print(day2_part2(test_input))