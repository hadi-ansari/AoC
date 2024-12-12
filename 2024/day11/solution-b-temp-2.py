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

@functools.cache
def do_once(stones):
    # print("calculating...")
    final = []
    for k in range(len(stones)):
        new_temp = blink(stones[k])
        final.extend(new_temp)

    return final

@functools.cache
def do_25(number):
    # print("doing 25 times")
    temp = [number]
    for k in range(25):
        # print("#"*15, "do_once start", "#"*15)
        temp = do_once(sort_list(tuple(temp)))
        # print("#"*15, "do_once end", "#"*15)
        
    return temp


@functools.cache
def sort_list(lst):
    return tuple(sorted(lst, key=len))


def main():
    # stones = read_problem("input-example-2.txt")
    stones = read_problem("input.txt")
    final = stones

    print(final)
    for i in range(1):
        temp_final = []
        for f in final:
            # print("*"*15, "do_25 START", "*"*15)
            res = do_25(f)
            # print("*"*15, "do_25 END", "*"*15)

            temp_final.extend(res)

        final = temp_final
        
    print("sum => ", len(final))

main()