def get_input() -> list:
    with open(r'AOC2021/day01input.txt', 'r') as file:
        file_list = file.read().splitlines()
        num_list = [int(i) for i in file_list]
    return num_list

def partOne(nums):
    cnt = 0
    for f, b in zip(nums[:-1], nums[1:]):
        if f < b:
            cnt += 1
    return cnt

def partTwo(nums):
    chunks = [nums[i:i+3] for i in range(len(nums) - 2)]
    cnt = 0
    for f,b in zip(chunks[:-1], chunks[1:]):
        if sum(f) < sum(b):
            cnt += 1
    return cnt

def main():
    nums = get_input()
    print(f"The answer to part 1 is {partOne(nums)}")
    print(f"The answer to part 2 is {partTwo(nums)}")

if __name__ == '__main__':
    main()
