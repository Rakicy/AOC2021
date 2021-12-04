import numpy as np
def get_input() -> list:
    with open(r'AOC2021/day03input.txt', 'r') as file:
        file_list = np.array([[int(j) for j in i] for i in file.read().splitlines()])
    return file_list

def partOne(bin_arr):
    gamma, epsilon = '',''
    for i in range(len(bin_arr[0])):
        ones = sum(bin_arr[:,i])
        zeros = len(bin_arr[:,:]) - ones
        if ones > zeros:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    return int(gamma, 2) * int(epsilon, 2)

def partTwo(bin_arr):
    ox, co = 0, 0
    new_bin_arr = bin_arr
    for i in range(len(bin_arr[0])):
        cur_list = np.array(new_bin_arr[:,i])
        if one_most_comm(cur_list):
            filter_arr = cur_list == 1
            new_bin_arr = new_bin_arr[filter_arr]
        else:
            filter_arr = cur_list == 0
            new_bin_arr = new_bin_arr[filter_arr]
        if len(new_bin_arr) == 1:
            ox_str = ''
            for i in new_bin_arr[0]:
                ox_str += str(i)
            ox = int(ox_str,2)
            break
    new_bin_arr = bin_arr
    for i in range(len(bin_arr[0])):
        cur_list = new_bin_arr[:,i]
        if one_most_comm(cur_list):
            filter_arr = cur_list != 1
            new_bin_arr = new_bin_arr[filter_arr]
        else:
            filter_arr = cur_list != 0
            new_bin_arr = new_bin_arr[filter_arr]
        if len(new_bin_arr) == 1:
            co_str = ''
            for i in new_bin_arr[0]:
                co_str += str(i)
            co = int(co_str,2)
            break
    return ox * co

def one_most_comm(bin_list):
    ones = sum(bin_list)
    zeros = len(bin_list) - ones
    if ones >= zeros:
        return True
    else:
        return False

def main():
    dims = get_input()
    print(f"The answer to part 1 is {partOne(dims)}")
    print(f"The answer to part 2 is {partTwo(dims)}")

if __name__ == '__main__':
    main()
