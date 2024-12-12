from reader import read_problem
import functools

@functools.cache
def blink(number_str):
    new_stones = []
    if int(number_str) == 0:
        new_stones = ["1"]
    elif len(number_str) % 2 == 0:
        left_half = number_str[:len(number_str) // 2]
        right_half = number_str[len(number_str)//2:] 

        new_stones =[str(int(right_half)), str(int(left_half))]
    else:
        new_stones = [str(int(number_str) * 2024)]

    return new_stones

def do_once(stones):
    final = {}
    for k in stones:
        new_temp = blink(k)
        for n in new_temp:
            if n in final:
                final[n] += stones[k]
            else:
                final[n] = stones[k]

    return final

def solve_75(hash):
    temp = hash
    for k in range(75):
        temp = do_once(temp)

    sum = 0
    for i in temp:
        sum += temp[i]

    print("sum => ", sum)


def main():
    stones = read_problem("input.txt")

    final_hash = {}
    for s in stones:
        if s in final_hash:
            final_hash[s] += 1
        else:
            final_hash[s] = 1

    solve_75(final_hash)
        
main()