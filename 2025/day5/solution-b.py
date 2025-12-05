from reader import read_problem

def is_inner_range(curr, prev):
    if curr.start in prev and (curr.stop - 1) in prev:
        return True
    return False

def overlap(curr, prev):
    print("Calculating overlap for: ({}, {}) and ({}, {})".format(curr.start, curr.stop - 1, prev.start, prev.stop - 1))
    start_range = max(curr.start, prev.start)
    end_range = min(curr.stop, prev.stop)


    if end_range < start_range or not (start_range in curr and start_range in prev and end_range - 1  in curr and end_range - 1 in prev):
        print("No overlap")
        return 0, False, ()

    overlap_len = end_range - start_range

    # print("Current length:", curr_len, "Intersection length:", inter_len)
    print("Overlap found ({}, {}), length: {}".format(start_range, end_range - 1, overlap_len))
    return overlap_len, True, range(start_range, end_range)

def update_range(overlap_range, r):
    if overlap_range.start == r.start and overlap_range.stop == r.stop:
        print("Removing entire range ({}, {})".format(r.start, r.stop - 1))
        return range(0, 1) 
    
    if overlap_range.start >= r.start and overlap_range.stop <= r.stop:
        return range(r.start, overlap_range.start)
    
    if overlap_range.stop <= r.stop and overlap_range.start >= r.start:
        return range(overlap_range.stop, r.stop)
    
    return r

def solve(ranges):
        sum = 0

        for current_range in ranges:
            print("Processing range: ({}, {}) lenght: {} ".format(current_range.start, current_range.stop - 1, len(current_range)))
            print("**********************************")
            sum += len(current_range)
           
        sum_overlaps = 0
        for i in range(len(ranges)):
            if i == range(0,1):
                continue
            print("Processing range: ({}, {}) ".format(ranges[i].start, ranges[i].stop - 1))

            for j in range(len(ranges)):
                if i == j or j == range(0,1):
                    continue
                
                overlap_len, has_overlap, overlap_range = overlap(ranges[i], ranges[j])
                if has_overlap:
                    sum_overlaps += overlap_len

                    res = update_range(overlap_range, ranges[i])
                    print("Updating range ({}, {}) to ({}, {}) ".format(ranges[i].start, ranges[i].stop - 1, res.start, res.stop - 1))
                    ranges[i] = res

        # print("Initial sum of fresh items (with overlaps):", sum)

        # print("Sum of overlaps:", sum_overlaps)

        # print("Sum of fresh items:", sum - sum_overlaps // 2)

def main():
    for i in range(5, 6):
        print("===================================")
        print("Processing input-example-{}.txt".format(i))
        print("===================================")
        file_name = "input-example-{}.txt".format(i)
        ranges, _ = read_problem(file_name)

        solve(ranges)
        

    # ranges, _ = read_problem("input.txt")
    # solve(ranges)

main()