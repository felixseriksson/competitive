for case in range(int(input())):
    string = [int(x) for x in input()]
    if not (1 in string):
        print(1)
    elif not (0 in string):
        print(0)
    else:
        ohone = False
        oneoh = False
        for i in range(len(string)-1):
            if ohone and oneoh:
                break
            if string[i] == 0 and string[i+1] == 1:
                ohone = True
            elif string[i] == 1 and string[i+1] == 0 and ohone:
                oneoh = True
        if oneoh and ohone:
            print(2)
        else:
            print(1)