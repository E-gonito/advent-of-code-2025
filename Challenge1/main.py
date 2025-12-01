
def main():
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



if __name__ == "__main__":
    main()
