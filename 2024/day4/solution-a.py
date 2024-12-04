from reader import read_problem
import re 

def find_XMAS(line):
    result = re.findall("XMAS", line)
    return len(result)

def main():
    lines = read_problem("input.txt")
    line_lenght = len(lines[0])

    sum = 0

    for line in lines:
        sum += find_XMAS(line.strip())
        sum += find_XMAS(line.strip()[::-1])

    columns = []

    for i in range(line_lenght):
        temp = ""
        for j in range(len(lines)):
            temp += lines[j][i]
        columns.append(temp)

    for col in columns:
        sum += find_XMAS(col.strip())
        sum += find_XMAS(col.strip()[::-1])

    diagonal_line_down = []

    for k in range(len(lines)):
        row_idx = 0
        col_idx = k
        temp = ""
        while row_idx < line_lenght and col_idx < len(lines):
            temp += lines[col_idx][row_idx]
            row_idx += 1
            col_idx += 1
        if len(temp) > 3:
            diagonal_line_down.append(temp)


    for a in diagonal_line_down:
        sum += find_XMAS(a)
        sum += find_XMAS(a[::-1])

    diagonal_line_right = []


    for k in range(1, line_lenght - 1):
        row_idx = k
        col_idx = 0
        temp = ""
        for j in range(min(line_lenght - row_idx, len(lines) - col_idx)):
            temp += lines[col_idx][row_idx]
            row_idx += 1
            col_idx += 1
        if len(temp) > 3:
            diagonal_line_right.append(temp)
        


    for b in diagonal_line_right:
        sum += find_XMAS(b)
        sum += find_XMAS(b[::-1])

    ## Reverse 
    reverse_lines = []
    for l in lines:
        reverse_lines.append(l[::-1])

    diagonal_line_down = []

    for k in range(len(reverse_lines)):
        row_idx = 0
        col_idx = k
        temp = ""
        while row_idx < line_lenght and col_idx < len(reverse_lines):
            temp += reverse_lines[col_idx][row_idx]
            row_idx += 1
            col_idx += 1
        if len(temp) > 3:
            diagonal_line_down.append(temp)
        
    for a in diagonal_line_down:
        sum += find_XMAS(a)
        sum += find_XMAS(a[::-1])


    diagonal_line_right = []


    for k in range(1, line_lenght - 1):
        row_idx = k
        col_idx = 0
        temp = ""
        for j in range(min(line_lenght - row_idx, len(reverse_lines) - col_idx)):
            temp += reverse_lines[col_idx][row_idx]
            row_idx += 1
            col_idx += 1
        if len(temp) > 3:
            diagonal_line_right.append(temp)
        
    for b in diagonal_line_right:
        sum += find_XMAS(b)
        sum += find_XMAS(b[::-1])

    
    print(sum)

main()