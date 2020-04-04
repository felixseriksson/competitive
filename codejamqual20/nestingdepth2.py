# bättre idé: håll löpande koll på skillnaden mellan två siffror, infoga så många parenteser som skillnaden är och åt rätt håll
testcases = int(input())
for testcase in range(1, testcases+1):
    # kod
    string = [int(char) for char in input()]
    string.insert(0, 0)
    string.append(0)
    final = ""
    for index in range(len(string)-1):
        final += str(string[index])
        diff = string[index+1]-string[index]
        final += diff * "(" if diff >= 0 else -diff * ")"
    print("Case #{}: {}".format(testcase, final[1:]))