from reader import read_problem

def main():
    reports = read_problem("input.txt")
    total_safe = 0
    for report in reports:
        report_list = list(map(int, report.split()))
        increasing = False
        decreasing = False

        if report_list[0] > report_list[1]:
            decreasing = True
        else:
            increasing = True

        for i in range(len(report_list)):
            if i == len(report_list) - 1:
                total_safe += 1
                break

            if abs(report_list[i] - report_list[i + 1]) > 3 or report_list[i] == report_list[i + 1]:
                break
            
            if increasing and report_list[i] > report_list[i + 1]:
                break
            elif decreasing and report_list[i] < report_list[i + 1]:
                break

    print("Total => ", total_safe)    

main()