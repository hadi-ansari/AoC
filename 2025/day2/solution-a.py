from reader import read_problem

def has_repeat(id):
    str_id = str(id)

    if len(str_id) % 2 != 0:
        return False
    
    first_half = str_id[0:len(str_id)//2]
    second_half = str_id[len(str_id)//2:len(str_id)]

    return first_half == second_half


def main():
    ranges = read_problem("input.txt")
    sum = 0
    for r in ranges:
        first_id = int(r.split("-")[0])
        last_id = int(r.split("-")[1])

        for i in range(first_id, last_id + 1):
            if has_repeat(i):
                sum += i
        
    print("Total IDs with repeats: {}".format(sum))

main()