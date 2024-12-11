from reader import read_problem
import copy

def blink(stones):
    new_stones = copy.deepcopy(stones)
    diff = 0
    for i in range(len(stones)):
        curr_idx = i + diff
        if int(stones[i]) == 0:
            new_stones[curr_idx] = "1"
            
        elif len(stones[i]) % 2 == 0:

            left_half = stones[i][:len(stones[i]) // 2]
            right_half = stones[i][len(stones[i])//2:] 

            new_stones[curr_idx] = str(int(right_half))
            new_stones.insert(curr_idx, str(int(left_half)))

            diff += 1
            
        else:
            new_stones[curr_idx] = str(int(stones[i]) * 2024)


    return new_stones

def main():
    stones = read_problem("input.txt")

    for i in range(25):
        stones = blink(stones)

    
    print("sum => ", len(stones))

main()