import numpy as np
def get_input() -> list:
    data = np.genfromtxt(r'AOC2021/day06input.txt', delimiter=',', dtype=int)
    return data

def partOne(pop_rate, pop_time):
    for _ in range(pop_time):
        born = len(pop_rate[pop_rate == 0])
        born_arr = np.array([8] * born, dtype=int)
        pop_rate = pop_rate - 1
        pop_rate[pop_rate < 0] = 6
        pop_rate = np.append(pop_rate, born_arr)
    return len(pop_rate)

def partTwo(pop_rate, pop_time):
    rate = dict()
    for i in range(9):
        rate[i] = 0
        rate[i] = len(pop_rate[pop_rate == i])
    temp = dict()
    for _ in range(pop_time):
        for i in range(0,8):
            temp[i] = rate[i+1]
        temp[8] = rate[0]
        temp[6] += rate[0]
        rate = temp.copy()
    return sum(rate.values())

def main():
    pop_rate = get_input()
    print(f"The answer to part 1 is {partOne(pop_rate, 80)}")
    print(f"The answer to part 2 is {partTwo(pop_rate, 256)}")

if __name__ == '__main__':
    main()
