from reader import read_problem
import copy 

def main():
    diskmap = read_problem("input.txt")
    sum = 0
    curr_idx = 0
    
    for i in range(len(diskmap)):
        if diskmap[i] == -1:
            break
        if i % 2 == 0:
            if diskmap[i] == -1:
                break
            block_id = i // 2
            for k in range(diskmap[i]):
                sum += (curr_idx * block_id)
                curr_idx += 1

        else:
            curr = diskmap[i]
            for j in range(len(diskmap) - 1, i, -1):
                if curr <= 0:
                    break
                if diskmap[j] == -1 or curr == 0:
                    continue
                if j % 2 == 0:
                    block_id = j // 2
                    if diskmap[j] > curr:
                        for k in range(curr):
                            sum += (curr_idx * block_id)
                            curr_idx += 1
                        diskmap[j] = (diskmap[j] - curr)
                        break
                    elif diskmap[j] == curr:
                        for k in range(curr):
                            sum += (curr_idx* block_id)
                            curr_idx += 1
                        diskmap[j] = -1
                        break
                    elif diskmap[j] < curr:
                        for k in range(diskmap[j]):
                            sum += (curr_idx * block_id)
                            curr_idx += 1
                        curr -= diskmap[j]
                        diskmap[j] = -1

    print("sum => ", sum)

main()