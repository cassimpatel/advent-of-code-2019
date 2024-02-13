def parse_input(input):
    nums = [int(x) for x in input.split('-')]
    return nums[0], nums[1]

def valid_passwords(low, high, part_2 = False):
    # take all 6 length strings
    passwords = [str(x) for x in range(100000, 1000000)]

    # take only passwords in the range
    passwords = [x for x in passwords if low <= int(x) <= high]

    # remove passwords where digits decrease
    def non_dec(s):
        for i in range(1, 6):
            if s[i] < s[i-1]:
                return False
        return True
    passwords = [x for x in passwords if non_dec(x)]

    # take only passwords with two adj digits the same
    def adj_same(s):
        for i in range(1, 6):
            if s[i] == s[i-1]:
                return True
        return False
    passwords = [x for x in passwords if adj_same(x)]

    if not part_2:
        return passwords

    # take only passwords where the two adjacent matching digits is not part of a larger group
    def adj_same_no_larger(s):
        for i in range(1, 6):
            if s[i] == s[i-1] and f'{s[i]}{s[i]}{s[i]}' not in s:
                return True
        return False
    passwords = [x for x in passwords if adj_same_no_larger(x)]

    return passwords

def day4_part1(input):
    low, high = parse_input(input)
    passwords = valid_passwords(low, high)
    return len(passwords)

def day4_part2(input):
    low, high = parse_input(input)
    passwords = valid_passwords(low, high, True)
    return len(passwords)

if __name__ == "__main__":
    test_input = open('input.txt', 'r').read()

    print(day4_part1(test_input))
    print(day4_part2(test_input))