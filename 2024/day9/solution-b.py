from reader import read_problem
import copy 

def build_initial_list(m):
    final_list = []
    for i in range(len(m)):
        if i % 2 == 0:
            block_id = i // 2
            temp = [] 
            for j in range(m[i]):
                temp.append(str(block_id))
            final_list.append(temp)
        else:
            temp = [] 
            for j in range(m[i]):
                temp.append(".")
            final_list.append(temp)
    
    return final_list

def update_final_list(final_list, free_spot_idx, file_idx):
    res = final_list
    file_len = len(final_list[file_idx])


    file_list = copy.deepcopy(final_list[file_idx])
    free_list = copy.deepcopy(final_list[free_spot_idx])

    for i in range(len(final_list[free_spot_idx])):
        if free_list[i] == "." and len(file_list) > 0:
            # print("OK")
            free_list[i] = file_list[0]
            del file_list[0]


    new_free_list_for_file = []
    for i in range(file_len):
        new_free_list_for_file.append(".")
    res[file_idx] = new_free_list_for_file
    res[free_spot_idx] = free_list

    return res


def main():
    diskmap = read_problem("input.txt")
    sum = 0
    final_list = build_initial_list(diskmap)

    for i in range(len(final_list) - 1, -1, -1):
        if i % 2 == 0:
            file_size = len(final_list[i])
           
            for j in range(i):
                if j % 2 == 1:
                     file_idx = i
                     free_spot_idx = j
                     span_len =  0
                     for o in final_list[j]:
                         if o == ".":
                             span_len += 1

                     if span_len >= file_size:
                        final_list = update_final_list(final_list, free_spot_idx, file_idx)

    str = ""
    counter = 0
    for i in final_list:
        for j in i:
            str += j
            if j != ".":
                sum += int(j) * counter
            counter += 1

    print("sum => ", sum)

main()