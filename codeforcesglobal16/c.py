for case in range(int(input())):
    n = int(input())
    string1 = [int(x) for x in input()]
    string2 = [int(x) for x in input()]
    string = [(string1[i], string2[i]) for i in range(n)]
    summ = 0
    onesflag = False
    zeroflag = False
    for idx in range(n):
        a = string[idx][0]
        b = string[idx][1]
        if (a == 0 and b == 1) or (a == 1 and b == 0):
            summ += 2
            if zeroflag:
                summ += 1
            onesflag = False
            zeroflag = False
        elif a == 1 and b == 1:
            if zeroflag:
                summ += 2
                zeroflag = False
            elif onesflag:
                pass
            else:
                onesflag = True
        else:
            # if a == 0 and b == 0
            if onesflag:
                summ += 2
                onesflag = False
            elif zeroflag:
                summ += 1
            else:
                zeroflag = True
    if zeroflag:
        summ += 1
    print(summ)
