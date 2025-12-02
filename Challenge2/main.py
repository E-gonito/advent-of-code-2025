def part1():
    with open('puzzleinput.txt', 'r') as f:
        invalid_id = 0
        f = f.read().split(",")
        for id_range in f:
            lower = int(id_range.split("-")[0])
            upper = int(id_range.split("-")[1])
            for x in range(lower, upper + 1):
                x_len = len(str(x))
                if x_len % 2 == 0 and (str(x)[0:x_len//2] == str(x)[x_len//2:]) :
                    invalid_id += x
    print(invalid_id)
    return invalid_id




if __name__ == "__main__":
    part1()
