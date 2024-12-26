INCREMENT_PATTENR = {
    4: (10650, [8192,1383,8,6801,8192,1383,8,6801,8192,1383,8,5120,1681,2415,5522,255,1383,8,6801]),
    5: (62217, [30353,100719,131072,30353,100719,71058,255,1383,8,31377,1383,8,25600,5522,255,1383,8,23185,8192,1383,8,91136,131072,30353,100719,131072]),
    6: (3705242,[1383,8,25600,262144,2823570,255,1383,8,1079953,1383,8,25600,262144,2922129,1383,8,981649,1383,8,25600,38545,1383,8,222208,2823570,255,1383,8,1079953,1383,8,25600,262144,292497,262144,237313,255,1383,8,23185,262144,262144,262144,237313,255,1383,8,23185,262144,262144,262144,237313,255,1383,8,23185,262144,262144,262144,204800,1383,8,25600,5522,255,1383,8,23185,231791,30353,2793217,255,1383,8,1079953,1383,8,25600,262144,2922129,1383,8,981649,1383,8,25600,38545,1383,8,222208,2823570,255,1383,8,1079953,1383,8,25600,262144,3905169]),
    7: (6817947, [255,1383,8,4291217,1383,8,4094354,255,1383,8,1661585,499457,255,1383,8,23185,262144,1310720,499457,255,1383,8,23185,262144,262144,3579649]),
    8: (153184666, [786432,262144,198180864,69206016,786432,262144,267386880,786432,262144,121020161,255,1383,8,16775570,255,1383,8,60381841,69206016,786432,262144,267386880]),
    9: (690055578,[786432,262144,1194761985,255,1383,8,951671441,786432,262144,2146435072,786432,262144,1194761985,255,1383,8,951671441,786432,262144,2146435072]),
    10: (2837539226, [786432,262144,2146435072]),
    11: (2837539226, [786432,262144,2146435072]),
    12: (15722441114, [786432,262144,68718428160]),
    13: (428039301530, [786432,262144,68718428160,786432,262144,1030791102464]),
    14: (2695782033818,[786432,262144,2130302730240,786432,262144,68718428160,786432,262144,2199022206976]),
   }

def decimal_to_binary(num):
    binary = []
    div = num
    while True:
        if div < 2:
            binary.append(div)
            break
        
        remainder = div % 2
        binary.append(remainder)
        div = div // 2

    binary.reverse()
    return "".join(str(bit) for bit in binary)

def binary_to_decimal(num):
    res = 0
    num = num[::-1]
    for i in range(len(num)):
        res += (int(num[i]) * (2 ** i))
    return res

def xor_decimal(num1, num2):
    xor_result = ""
    first_num = decimal_to_binary(num1)
    second_num = decimal_to_binary(num2)

    if len(first_num) > len(second_num):
        diff = len(first_num) - len(second_num)
        second_num = "0" * diff + second_num
    elif len(first_num) < len(second_num):
        diff = len(second_num) - len(first_num)
        first_num = "0" * diff + first_num

    for i in range(len(first_num)):
        first_c = first_num[i]
        second_c = second_num[i]

        if first_c != second_c:
            xor_result += "1"
        else:
            xor_result += "0"

    return binary_to_decimal(xor_result)

def calculate(a, num):
    temp_a = a
    b = temp_a % 8
    b = xor_decimal(b, 5)
    c = temp_a // 2 ** b
    b = xor_decimal(b, 6)
    temp_a = temp_a // 8
    b = xor_decimal(b, c)
    out = b % 8
    
    if out != num:
        return None
    else:
        return a // 8

# Expected 2,4,1,5,7,5,1,6,0,3,4,1,5,5,3,0
def main():
    # change these to 4 to find the first pattern in which i should increment
    num = 14

    # uncomment these for finding the pattern in which i should increment
    # prev = None
    # res = []

    cur = INCREMENT_PATTENR[num][0]
    i = 0
    while True:
        a2 = calculate(cur, 2)
        if a2:
           a4 = calculate(a2, 4)
           if a4:
            ##################################################################################################
            #
            # By doing the following lines you find the pattern in which the i should increment
            # After finding this for second number updare the num and find for the third number 
            # by moving these line one step down in the if statement chain
            # and comment out the rest of the lines
                # if prev:
                #     res.append(cur - prev)
                # else:
                #     res.append(cur)
                # if len(res) > 50:
                #     break
            #
           ##################################################################################################
                a1 = calculate(a4, 1)
                if a1:
                    a5 = calculate(a1, 5)
                    if a5:
                        a7 = calculate(a5, 7)
                        if a7:
                            a5 = calculate(a7, 5)
                            if a5:
                                a1 = calculate(a5, 1)
                                if a1:
                                    a6 = calculate(a1, 6)
                                    if a6:
                                        a0 = calculate(a6, 0)
                                        if a0:
                                            a3 = calculate(a0, 3)
                                            if a3:
                                                a4 = calculate(a3, 4)
                                                if a4:
                                                    a1 = calculate(a4, 1)
                                                    if a1:
                                                        a5 = calculate(a1, 5)
                                                        if a5:
                                                            a5 = calculate(a5, 5)
                                                            if a5:
                                                                a3 = calculate(a5, 3)
                                                                if a3:
                                                                    a0 = calculate(a3, 0)
                                                                    if a0 != None and a0 == 0:
                                                                        print("{} works for 0".format(cur))
                                                                        return

        if i > len(INCREMENT_PATTENR[num][1]) - 1:
            i = 0
        cur += INCREMENT_PATTENR[num][1][i]
        i += 1

    # These are for finding the pattern when you comment in the code above
    # you should uncomment these too, to find the pattern
    # res = [str(x) for x in res]
    # print(",".join(res))


# It seems that all output have a pattern which repeats. To shorten the search
# I have found how long each step should increment instead of iterating for all numbers form
# 0 to the answer 105981155568026. By finding the 
main()