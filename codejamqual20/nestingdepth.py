# princip: hitta max, sätt ut parenteser runt dessa, räkna dessa som utan parenteser men värde ett lägre, upprepa, när alla är 0, bryt
# ex: 1234321 -> 123(4)321 -> 1233321 -> 12(333)21 -> 1222221 -> 1(22222)1 -> 1111111 -> (1111111) == (1(2(3(4)3)2)1)
# edit: nvm, detta är korkat det går att göra mycket smartare och snabbare, se nestingdepth2.py

testcases = int(input())
for testcase in range(1, testcases+1):
    #kör kod
    string = [char for char in input()]
    string.insert(0, "0")
    string.append("0")
    final = string[::]
    while len(set(string)) != 1:
        maxdigit = max(string)
        index = 0
        maxlim = len(final)
        while True:
            if index == maxlim:
                break
            if final[index] != maxdigit:
                index += 1
                continue
            else:
                if final[index-1] != maxdigit:
                    # första av sin sort
                    final.insert(index, "(")
                    string.insert(index, str(str(int(maxdigit)-1)))
                    index += 1
                    maxlim += 1
                    string[index] = str(int(maxdigit)-1)
                if final[index+1] != maxdigit:
                    # sista av sin sort
                    final.insert(index+1, ")")
                    string.insert(index+1, str(str(int(maxdigit)-1)))
                    maxlim += 1
                    string[index] = str(int(maxdigit)-1)
                else:
                    #nånstans i mitten
                    string[index] = str(int(maxdigit)-1)
                index += 1
            # print(string)
            # print(final)

    print("Case #{}: {}".format(testcase, "".join(final[1:-1])))
