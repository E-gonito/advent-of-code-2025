def part1():
    with open('puzzleinput.txt', 'r') as f:
        joltage_sum = 0
        for line in f.read().strip().split('\n'):
            first_pos = line.index(max(line[:-1]))
            second_pos = line.index(max(line[first_pos+1:]))
            joltage_sum += int(line[first_pos]) * 10 + int(line[second_pos])
        print(joltage_sum)
        
def part2():
    with open('puzzleinput.txt', 'r') as f:
        joltage_sum = 0
        for line in f.read().strip().split('\n'):
            

        


if __name__ == "__main__":
    part1()
