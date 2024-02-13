def parse_input(input):
    return [int(x) for x in input]

def day8_part1(input, w=25, h=6):
    input = parse_input(input)

    layer_size = w * h
    num_layers = len(input) // layer_size

    layers = []
    for i in range(num_layers):
        layers.append(input[i * layer_size: (i + 1) * layer_size])

    layers.sort(key = lambda x: x.count(0))
    min_layer = layers[0]
    return min_layer.count(1) * min_layer.count(2)

def day8_part2(input, w=25, h=6):
    input = parse_input(input)
    layer_size = w * h
    num_layers = len(input) // layer_size
    
    image = []
    for pix in range(layer_size):
        for layer in range(num_layers):
            val = input[layer * layer_size + pix]
            if val == 2: continue
            image.append(val)
            break
    
    res = '█' * (w + 2) + '\n'
    for y in range(h):
        res += '█'
        for x in range(w):
            v = image[y*w+x]
            res += (' ' if v == 1 else '█')
        res += '█\n'
    res += '█' * (w + 2) + '\n'

    return res

if __name__ == "__main__":
    example_input_1 = '123456789012'
    example_input_2 = '0222112222120000'
    test_input = open('input.txt', 'r').read()

    assert day8_part1(example_input_1, 3, 2) == 1
    print(day8_part1(test_input))

    assert day8_part2(example_input_2, 2, 2) == '████\n██ █\n█ ██\n████\n'
    print(day8_part2(test_input))