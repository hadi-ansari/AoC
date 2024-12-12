from reader import read_problem
import copy
import functools

@functools.cache
def do_it(stones):
    final = []
    sum = 0
    for k in range(len(stones)):
        new_temp = blink(stones[k])
        for n in new_temp:
            final.append(n)
        sum += len(new_temp)
    return final, sum


@functools.cache
def blink(number_str):
    stones = [number_str]
    new_stones = copy.deepcopy(stones)
    diff = 0
    for i in range(len(stones)):
        curr_idx = i + diff
        if int(stones[i]) == 0:
            # print("replace {} with one".format(stones[i]))
            new_stones[curr_idx] = "1"
        elif len(stones[i]) % 2 == 0:
            # print("split {} in half".format(stones[i]))
            left_half = stones[i][:len(stones[i]) // 2]
            right_half = stones[i][len(stones[i])//2:] 

            new_stones[curr_idx] = str(int(right_half))
            new_stones.insert(curr_idx, str(int(left_half)))

            diff += 1

            # print("left half {}".format(left_half))
            # print("right half {}".format(right_half))
            # print(new_stones)         
        else:
            # print("multiply {} with 2024".format(stones[i]))
            new_stones[curr_idx] = str(int(stones[i]) * 2024)


    return new_stones

def recursive_fun(ls):
    if len(ls) == 0:
        return []
    if len(ls) == 1:
        temp = blink(ls[0])
        return temp
    else:
        temp = []
        temp2 = blink(ls[0])
        for t2 in temp2:
            temp.append(t2)

        # print("calc this => ", ls[1:])
        temp_rest = recursive_fun(ls[1:])

        for tr in temp_rest:
            temp.append(tr)

        return temp
    


def main():
    stones = read_problem("input.txt")
    final = stones

    print(final)

    for i in range(25):
        final, sum = do_it(tuple(final))

            
    print("sum => ", sum)

main()