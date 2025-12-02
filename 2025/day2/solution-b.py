from reader import read_problem

def has_repeat(id):
    str_id = str(id)

    number_of_matches = 1
    for i in range(1, len(str_id)//2 + 1):
        if number_of_matches > 1:
            return True
        pattern = str_id[0:i]
        for j in range(i, len(str_id), i):
            if str_id[j:i+j] == pattern:
                number_of_matches += 1
            else:
                number_of_matches = 1
                break
    
    if number_of_matches > 1:
        return True

    return False


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