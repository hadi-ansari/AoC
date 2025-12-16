from reader import read_problem

def solve(devices):
    sum_of_path = 0
    q = []
    for output in devices["you"]:
        q.append(output)

    while len(q) > 0:
        curr = q.pop()
        if devices[curr][0] == "out":
            sum_of_path += 1
        else:
            for output in devices[curr]:
                q.append(output)
    
    return sum_of_path


def main():
    sum = 0
    devices = read_problem("input.txt")

    sum = solve(devices)
    print("Answer {}".format(sum))
    
main()