from reader import read_problem
from itertools import combinations, combinations_with_replacement, product

LIFHTS_INDEX = 0
BUTTONS_INDEX = 1
JOLTAGES_INDEX = 2

def print_combo(combo):
    combo_len = len(list(combo))
    print()
    print("Combo with lenght {}".format(combo_len))
    print("=" * 20)
    for c in combo:
        print(c)
    print()
    print("=" * 20)

def print_product(product):
    combo_len = len(list(product))
    print()
    print("Product with lenght {}".format(combo_len))
    print("*" * 20)
    for c in product:
        print(c)
    print()


def find_min(all_combos, joltages, verbose=False):
    min = 10000000000000
    for combos in all_combos:
        counter_number_of_presses = [0 for x in joltages]
        len_of_combo = len(combos)
        if verbose:
            print_product(combos)
        for item in combos:
            for num in item: # ()
                # print("num {}".format(num))
                counter_number_of_presses[num] += 1
        result_after_all_presses = [x % 10 for x in counter_number_of_presses]
        # print("Number of presses {}".format(counter_number_of_presses))
        # print("Result after all presses {}".format(result_after_all_presses))
        # # print("Goal {}".format(joltages))
        match = True
        for i in range(len(result_after_all_presses)):
            # print("joltages {} and result {}".format(joltages[i], result_after_all_presses[i]))
            if joltages[i] != result_after_all_presses[i]:
                match = False
                break
        if match and len_of_combo < min:
            # print("MATCH, len is {}".format(len_of_combo))
            result_after_all_presses = [x % 10 for x in counter_number_of_presses]

            min = len_of_combo

    return min

def find_min_two(combo, joltages, verbose=False):
    min = 10000000000000
    
    counter_number_of_presses = [0 for x in joltages]
    len_of_combo = 0
    for c in combo:
        len_of_combo += len(c)
        
    if verbose:
        print("len of combo {}".format(len_of_combo))

    if verbose:
        print_product(combo)
    for c in combo:
        for button in c:
            # print("button {}".format(button))
            for counter_num in button: # ()
                # print("counter num {}".format(counter_num))
                counter_number_of_presses[counter_num] += 1
    if verbose:
        print("Number of presses {}".format(counter_number_of_presses))
        print("Goal {}".format(joltages))
    match = True
    for i in range(len(counter_number_of_presses)):
        if joltages[i] != counter_number_of_presses[i]:
            match = False
            break
    if match and len_of_combo < min:
        # print("MATCH, len is {}".format(len_of_combo))

        min = len_of_combo

    return min

def solve(machine):
    min = 100000000000
    joltages = machine[JOLTAGES_INDEX]
    buttons = machine[BUTTONS_INDEX]

    max_joltage = max(joltages)
    # print(buttons)


    all_combos = []



    combo_list = []

    for b in buttons:
        temp = [b]
        temp_combos = []
        for k in range(1, max_joltage):
            inner_products = combinations_with_replacement(temp, k)
            for i in inner_products:
                # print_product(i)
                temp_combos.append(i)
                all_combos.append(i)
        combo_list.append(temp_combos)

    # print("ALL COMBOS")
    # print(all_combos)
    # print()

    new_min = find_min_two(all_combos, joltages)

    if new_min < min:
        min = new_min

    # new_min = find_min_two((((0,2,3,4), (0,2,3,4)), ((2,3),(2,3),(2,3),(2,3),(2,3)), ((0,1,2),(0,1,2),(0,1,2),(0,1,2),(0,1,2))), joltages, True)

    # return new_min
        
    # print("COMBO LIST")
    # for i in combo_list:
    #     print(i)


    for i in range(2, len(buttons) + 1):
        if i == len(buttons):
            verbose = True
        c = combinations(combo_list, i)
        for j in c:
            hello = product(*j)
            for k in hello:
                if False:
                    # print("Checking combination {}".format(k))
                    print("Len combination {}".format(len(k)))
                    
                new_min = find_min_two(k, joltages)
                if new_min < min:
                    min = new_min

    return min

def experiment():
    l1 = ["a", "aa", "aaa"]
    l2 = ["1", "11", "111"]
    l3 = ["X", "XX", "XXX"]
    l4 = ["😀", "😀😀", "😀😀😀"]
    combos = [l1, l2, l3, l4]

    for i in range(2, len(combos) + 1):
        print("lenght is {}".format(i))
        c = combinations(combos, i)
        for j in c:
            print(j)
            print("+"*50)
            hello = product(*j)
            for k in hello:
                print(k)
                
        print("=" * 50)
def main():

    # experiment()
    # return

    sum = 0
    machines = read_problem("input-example-2.txt")

    for m in machines:
        # print("Joltages: {}".format(m[JOLTAGES_INDEX]))
        # print("Buttons: {}".format(m[BUTTONS_INDEX]))
        sum += solve(m)

    print("Answer {}".format(sum))


main()