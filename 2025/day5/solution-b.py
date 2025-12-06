from readerb import read_problem
from functools import cmp_to_key

def solve(ranges):
    sum = 0
    sorted_ranges = []
    sorted_ranges = sorted(ranges, key=cmp_to_key(lambda a, b: a[0] - b[0]))
    new_ranges = []

    merged = False
    merge_result = None
    i = 0 
    while i < len(sorted_ranges) - 1:
        if merged and merge_result is not None:
            current_range = merge_result
        else:
            current_range = sorted_ranges[i]

        next_range = sorted_ranges[i + 1]
        if next_range[0] >= current_range[0] and next_range[1] <= current_range[1]:
            merge_result = current_range
            if merged:
                new_ranges.pop()
                new_ranges.append(merge_result)
            else:
                new_ranges.append(merge_result)
            merged = True


            
        elif next_range[0] <= current_range[1] and next_range[1] >= current_range[1]:
            merge_result = (min(current_range[0], next_range[0]), max(current_range[1], next_range[1]))
            if merged:
                new_ranges.pop()
                new_ranges.append(merge_result)
            else:
                new_ranges.append(merge_result)
            merged = True

        else:
            if not merged:
                new_ranges.append(current_range)
            merged = False
            merge_result = None

        if i == len(sorted_ranges) - 2 and not merged:
          new_ranges.append(next_range)
        
        i += 1

    
    for r in new_ranges:
        sum += (r[1] - r[0] + 1)

    print("Sum is ", sum)

def main():
    ranges, _ = read_problem("input.txt")
    solve(ranges)


main()