
def part1():
    with open('puzzleinput.txt', 'r') as f:
        dial = 50
        counter0 = 0
        for line in f:
            line = line.strip()
            direction = line[0]
            magnitude = int(line[1:])
            if direction == "R":
                dial += magnitude
            else:
                dial -= magnitude
            dial = dial % 100
            if dial == 0:
                counter0 += 1
    print(counter0)
    
def part2():
    with open('puzzleinput.txt', 'r') as f:
        dial = 50
        counter0 = 0
        for line in f:
            line = line.strip()
            direction = line[0]
            magnitude = int(line[1:])
            if dial == 0:
                counter0 += magnitude // 100
            if direction == "L":
                if magnitude >= dial and dial != 0:
                    counter0 += 1  # First crossing
                    remaining = magnitude - dial
                    counter0 += remaining // 100
                dial -= magnitude
            if direction == "R":
                if ( magnitude >= 100 - dial) and (dial != 0):
                    counter0 += 1  # First crossing
                    remaining = magnitude - (100 - dial)
                    counter0 += remaining // 100
                dial += magnitude
            dial = dial % 100
    print(counter0)
        
if __name__ == "__main__":
    part2()
