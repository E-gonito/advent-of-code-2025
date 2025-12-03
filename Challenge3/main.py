def part1():
    with open('puzzleinput.txt', 'r') as f:
        joltage_sum = 0
        for line in f.read().strip().split('\n'):
            first_pos = line.index(max(line[:-1]))
            second_pos = line.index(max(line[first_pos+1:]))
            joltage_sum += int(line[first_pos]) * 10 + int(line[second_pos])
        print(joltage_sum)
        
def part2():
    RESULT_LENGTH = 12
    with open('puzzleinput.txt', 'r') as f:
        joltage_sum = 0
        for line in f.read().strip().split('\n'):
            result = ""
            current_pos = -1 
            for current_digit in range(1, 13):
                start = current_pos + 1
                end = (len(line) - 1) - (RESULT_LENGTH - current_digit)
                search_window = line[start:end+1]
                max_digit = max(search_window)
                max_digit_pos = search_window.index(max_digit)
                current_pos = start + max_digit_pos
                result += line[current_pos]
            joltage_sum += int(result)
        print(joltage_sum)
            
            
            

        


if __name__ == "__main__":
    part2()
