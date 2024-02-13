def parse_input(input):
    return [int(x) for x in input.split(',')]

def run_prog(ins, input):
    ins = ins.copy()
    ins_pointer = 0
    output = []

    num_param = {
        1: 3,
        2: 3,
        3: 1,
        4: 1,
        99: 0
    }

    def extract_ins(pointer):
        cur_ins = ins[pointer]
        op_code = cur_ins % 100
        cur_ins //= 100

        params = []
        for i in range(num_param[op_code]):
            val = ins[pointer + i + 1]
            if cur_ins % 10  == 0:
                val = ins[val]
            params.append(val)
            cur_ins //= 10

        return op_code, tuple(params)

    while ins_pointer < len(ins):
        op_code, params = extract_ins(ins_pointer)

        if op_code == 1:
            (v1, v2, v3) = params
            v3 = ins[ins_pointer + 3]
            ins[v3] = v1 + v2
        elif op_code == 2:
            (v1, v2, v3) = params
            v3 = ins[ins_pointer + 3]
            ins[v3] = v1 * v2
        elif op_code == 3:
            (v1,) = params
            v1 = ins[ins_pointer + 1]
            ins[v1] = input.pop(0)
        elif op_code == 4:
            (v1,) = params
            output.append(v1)
        elif op_code == 99:
            break

        ins_pointer += num_param[op_code] + 1

    return output


def run_prog_v2(ins, input):
    ins = ins.copy()
    ins_pointer = 0
    output = []

    num_param = {
        1: 3,
        2: 3,
        3: 1,
        4: 1,
        5: 2,
        6: 2,
        7: 3,
        8: 3,
        99: 0
    }

    def extract_ins(pointer):
        cur_ins = ins[pointer]
        op_code = cur_ins % 100
        cur_ins //= 100

        params = []
        for i in range(num_param[op_code]):
            val = ins[pointer + i + 1]
            if cur_ins % 10  == 0:
                val = ins[val]
            params.append(val)
            cur_ins //= 10

        return op_code, tuple(params)

    while ins_pointer < len(ins):
        op_code, params = extract_ins(ins_pointer)

        if op_code == 1:
            (v1, v2, v3) = params
            v3 = ins[ins_pointer + 3]
            ins[v3] = v1 + v2
        elif op_code == 2:
            (v1, v2, v3) = params
            v3 = ins[ins_pointer + 3]
            ins[v3] = v1 * v2
        elif op_code == 3:
            (v1,) = params
            v1 = ins[ins_pointer + 1]
            ins[v1] = input.pop(0)
        elif op_code == 4:
            (v1,) = params
            output.append(v1)
        elif op_code == 5:
            (v1, v2) = params
            ins_pointer = v2 - (num_param[op_code] + 1) if v1 != 0 else ins_pointer
        elif op_code == 6:
            (v1, v2) = params
            ins_pointer = v2 - (num_param[op_code] + 1) if v1 == 0 else ins_pointer
        elif op_code == 7:
            (v1, v2, v3) = params
            v3 = ins[ins_pointer + 3]
            ins[v3] = 1 if v1 < v2 else 0
        elif op_code == 8:
            (v1, v2, v3) = params
            v3 = ins[ins_pointer + 3]
            ins[v3] = 1 if v1 == v2 else 0
        elif op_code == 99:
            break

        ins_pointer += num_param[op_code] + 1

    return output


def day5_part1(input):
    ins = parse_input(input)
    output = run_prog(ins, [1])
    return output[-1]

def day5_part2(input):
    ins = parse_input(input)
    output = run_prog_v2(ins, [5])
    return output[-1]

if __name__ == "__main__":
    test_input = open('input.txt', 'r').read()

    print(day5_part1(test_input))

    print(day5_part2(test_input))