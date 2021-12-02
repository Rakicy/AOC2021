import re
def get_input() -> list:
    with open(r'AOC2021/day02input.txt', 'r') as file:
        file_list = file.read()
    return file_list

def partOne(directions):
    f = sum(int(i) for i in re.findall(r'forward (\d)', directions))
    u = sum(int(i) for i in re.findall(r'up (\d)', directions))
    d = sum(int(i) for i in re.findall(r'down (\d)', directions))
    return f * (d - u)

def partTwo(directions):
    direct = [[i[0], int(i[-1])] for i in directions.splitlines()]
    aim = 0
    forward = 0
    depth = 0
    for i in direct:
        if i[0] == 'f':
            forward += i[1]
            depth += aim*i[1]
        elif i[0] == 'u':
            aim = max(0,aim - i[1])
        elif i[0] == 'd':
            aim += i[1]
    return forward * depth

def main():
    dims = get_input()
    print(f"The answer to part 1 is {partOne(dims)}")
    print(f"The answer to part 2 is {partTwo(dims)}")

if __name__ == '__main__':
    main()
