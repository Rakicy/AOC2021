import numpy as np
import sys

def get_input() -> list:
    with open(r'AOC2021/day07input.txt', 'r') as file:
        file_list = file.read().split(',')
    return [int(i) for i in file_list]

def partOne(nums):
    nums = np.array(nums)
    min_fuel = sys.maxsize
    ones_num = np.ones(nums.size, dtype=int)
    for i in range(min(nums), max(nums)+1):
        cur_num = ones_num * i
        cur_fuel = np.sum(np.abs(nums - cur_num))
        min_fuel = min(min_fuel, cur_fuel)
    return min_fuel

def partTwo(nums):
    nums = np.array(nums)
    min_fuel = sys.maxsize
    ones_num = np.ones(nums.size, dtype=int)
    for i in range(min(nums), max(nums)+1):
        cur_num = ones_num * i
        cur_fuel = np.abs(nums - cur_num)
        cur_fuel = np.sum(((cur_fuel ** 2) + cur_fuel)/2)
        min_fuel = min(min_fuel, cur_fuel)
    return int(min_fuel)

def main():
    nums = get_input()
    print(f"The answer to part 1 is {partOne(nums)}")
    print(f"The answer to part 2 is {partTwo(nums)}")

if __name__ == '__main__':
    main()
