def parse_input(input):
    [ins1, ins2] = [x.split(',') for x in input.split('\n')]
    dirs = {'U':(-1, 0), 'D':(1, 0), 'L':(0, -1), 'R':(0, 1)}

    points1 = set([(0,0)])
    y, x = 0, 0
    for ins in ins1:
        dy, dx = dirs[ins[0]]
        steps = int(ins[1:])
        for _ in range(steps):
            y += dy
            x += dx
            points1.add((y, x))
    
    points2 = set([(0,0)])
    y, x = 0, 0
    for ins in ins2:
        dy, dx = dirs[ins[0]]
        steps = int(ins[1:])
        for _ in range(steps):
            y += dy
            x += dx
            points2.add((y, x))

    return points1, points2, ins1, ins2

def steps_to_point(y, x, ins):
    cury = 0
    curx = 0
    res = 0

    dirs = {'U':(-1, 0), 'D':(1, 0), 'L':(0, -1), 'R':(0, 1)}
    for move in ins:
        dy, dx = dirs[move[0]]
        steps  = int(move[1:])
        for i in range(steps):
            cury += dy
            curx += dx
            if (cury, curx) == (y, x):
                return res + i + 1
        res += steps

def day3_part1(input):
    points1, points2, _, _ = parse_input(input)

    shared = points1.intersection(points2)
    shared.discard((0, 0))

    dists = [abs(a) + abs(b) for (a, b) in shared]
    return min(dists)

def day3_part2(input):
    points1, points2, ins1, ins2 = parse_input(input)

    shared = points1.intersection(points2)
    shared.discard((0, 0))

    dists = [steps_to_point(y, x, ins1) + steps_to_point(y, x, ins2) for (y, x) in shared]
    return min(dists)

if __name__ == "__main__":
    example_input_1 = open('example_1.txt', 'r').read()
    example_input_2 = open('example_2.txt', 'r').read()
    example_input_3 = open('example_3.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day3_part1(example_input_1) ==  6
    assert day3_part1(example_input_2) ==  159
    assert day3_part1(example_input_3) ==  135
    print(day3_part1(test_input))

    assert day3_part2(example_input_1) ==  30
    assert day3_part2(example_input_2) ==  610
    assert day3_part2(example_input_3) ==  410
    print(day3_part2(test_input))