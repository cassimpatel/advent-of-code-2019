def parse_input(input):
    return [int(x) for x in input.split(',')]

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


def day7_part1(input):
    ins = parse_input(input)
    comb = [0, 1, 2, 3, 4]
    res = 0
    
    def permute(l, r, curVal):
        if l == r:
            nonlocal res
            res = max(res, curVal)
            return

        for i in range(l, r):
            comb[l], comb[i] = comb[i], comb[l]
            out = run_prog_v2(ins, [comb[l], curVal])
            permute(l+1, r, out[-1])
            comb[l], comb[i] = comb[i], comb[l]
            
    permute(0, 5, 0)
    return res

def day7_part2(input):
    return None

if __name__ == "__main__":
    example_input_1 = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'
    example_input_2 = '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0'
    example_input_3 = '3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0'
    test_input = open('input.txt', 'r').read()

    assert day7_part1(example_input_1) == 43210
    assert day7_part1(example_input_2) == 54321
    assert day7_part1(example_input_3) == 65210
    print(day7_part1(test_input))

    # print(day7_part2(test_input))