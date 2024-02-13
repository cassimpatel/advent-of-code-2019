def parse_input(input):
    input = [x.split(')') for x in input.split('\n')]

    orbits = {b:a for [a, b] in input}

    has_orbitting = {}
    for [a, b] in input:
        has_orbitting[a] = has_orbitting.get(a, [])
        has_orbitting[b] = has_orbitting.get(b, [])
        has_orbitting[a].append(b)

    return orbits, has_orbitting


def day6_part1(input):
    orbits, _ = parse_input(input)

    total_orbits = {}
    def find_orbits(obj):
        if obj in total_orbits:
            return total_orbits[obj]
        if obj not in orbits:
            return 0

        total_orbits[obj] = 1 + find_orbits(orbits[obj])
        return total_orbits[obj]

    res = 0
    for obj in orbits:
        res += find_orbits(obj)

    return res

def day6_part2(input):
    orbits, has_orbitting = parse_input(input)

    src = orbits['YOU']
    dst = orbits['SAN']

    queue = [src]
    depth = 0
    vis = set()

    while queue:
        nxt_queue = []
        
        for obj in queue:
            if obj in vis: continue
            vis.add(obj)

            if obj == dst:
                return depth

            if orbits[obj] not in vis:
                nxt_queue.append(orbits[obj])
            for nxt in has_orbitting[obj]:
                if nxt in vis: continue
                nxt_queue.append(nxt)

        
        depth += 1
        queue = nxt_queue

    return None

if __name__ == "__main__":
    example_input_1 = open('example_1.txt', 'r').read()
    example_input_2 = open('example_2.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day6_part1(example_input_1) == 42
    print(day6_part1(test_input))

    assert day6_part2(example_input_2) == 4
    print(day6_part2(test_input))