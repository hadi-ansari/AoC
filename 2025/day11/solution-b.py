from reader import read_problem
import functools
import copy

cheat_sheet = {}
parent = {}
visited = set()

@functools.cache
def has_dac(path):
    return "dac" in path

@functools.cache
def has_fft(path):
    return "fft" in path

def check_path(current_path):
    current_path.insert(0, "svr")
    current_path.append("out")

    for i in range(1, len(current_path) - 1):
        step = current_path[i]
        sub_path = current_path[current_path.index(step): -1]
        if step not in cheat_sheet:
            cheat_sheet[step] = {"fft": 0, "dac": 0, "none": 0, "both": 0}
            if has_fft(tuple(sub_path)) and has_dac(tuple(sub_path)):
                cheat_sheet[step]["both"] = 1
            if has_fft(tuple(sub_path)):
                cheat_sheet[step]["fft"] = 1
            if has_dac(tuple(sub_path)):
                cheat_sheet[step]["dac"] = 1
            else:
                cheat_sheet[step]["none"] = 1
        else:
            if has_fft(tuple(sub_path)) and has_dac(tuple(sub_path)):
                cheat_sheet[step]["both"] += 1
            elif has_fft(tuple(sub_path)):
                cheat_sheet[step]["fft"] += 1
            elif has_dac(tuple(sub_path)):
                cheat_sheet[step]["dac"] += 1
            else:
                cheat_sheet[step]["none"] += 1

    
    if "dac" in current_path and "fft" in current_path:
        return True
    
    return False

def solve(devices):
    q = []
    current_path = set()
    sum_of_approved_paths = 0
    current_path = []
    for output in devices["svr"]:
        q.append(output)
        parent[output] = None

    while len(q) > 0:
        curr = q.pop()

        # Fix the current path
        if curr in parent and parent[curr]:
            current_path = current_path[0: current_path.index(parent[curr]) + 1]
        else:
            current_path = []

        if curr in visited:
            current_cheat = cheat_sheet[curr]
            if has_dac(tuple(current_path)):
                if current_cheat["fft"] > 0:
                    sum_of_approved_paths += current_cheat["fft"]

                dac_idx = current_path.index("dac")

                for i in range(len(current_path)):
                    step = current_path[i]
                    if step not in cheat_sheet:
                        cheat_sheet[step] = {"fft": 0, "dac": 0, "none": 0, "both": 0}
                    if i <= dac_idx:
                        cheat_sheet[step]["dac"] += current_cheat["none"]
                        cheat_sheet[step]["none"] -= current_cheat["none"]
                        cheat_sheet[step]["both"] += current_cheat["fft"]
                    else:
                        cheat_sheet[step]["fft"] += current_cheat["fft"]
                        cheat_sheet[step]["none"] += current_cheat["none"]

            elif has_fft(tuple(current_path)):
                if current_cheat["dac"] > 0:
                    sum_of_approved_paths += current_cheat["dac"]
                
                fft_idx = current_path.index("fft")
                for i in range(len(current_path)):
                    step = current_path[i]
                    if step not in cheat_sheet:
                        cheat_sheet[step] = {"fft": 0, "dac": 0, "none": 0, "both": 0}
                    if i <= fft_idx:
                        cheat_sheet[step]["fft"] += current_cheat["none"]
                        cheat_sheet[step]["fft"] -= current_cheat["dac"]
                        cheat_sheet[step]["both"] += current_cheat["dac"]
                    else:
                        cheat_sheet[step]["dac"] += current_cheat["dac"]
                        cheat_sheet[step]["none"] += current_cheat["none"]
                        cheat_sheet[step]["fft"] += current_cheat["fft"]
                    
            elif not has_dac(tuple(current_path)) and not has_fft(tuple(current_path)):
                sum_of_approved_paths += current_cheat["both"]

                for step in current_path:
                    if step not in cheat_sheet:
                        cheat_sheet[step] = {"fft": 0, "dac": 0, "none": 0, "both": 0}
                    cheat_sheet[step]["both"] += current_cheat["both"]
                    cheat_sheet[step]["dac"] += current_cheat["dac"]
                    cheat_sheet[step]["fft"] += current_cheat["fft"]
                    cheat_sheet[step]["none"] += current_cheat["none"]
            continue

        visited.add(curr)

        current_path.append(curr)
        
        if devices[curr][0] == "out":
            temp_path = copy.deepcopy(current_path)
            is_approved = check_path(temp_path)
            if is_approved:
                sum_of_approved_paths += 1
        else:
            for output in devices[curr]:
                if output not in current_path:
                    q.append(output)
                    parent[output] = curr

    return sum_of_approved_paths


def main():
    sum = 0
    devices = read_problem("input.txt")

    sum = solve(devices)
    print("Answer is {}".format(sum))
    
main()