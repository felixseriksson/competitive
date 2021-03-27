def sigm(x):
    return 1/(1+pow(e, -x))

cases, p = int(input()), int(input())
for case in range(1, cases+1):
    outcomes = [[int(x) for x in input()] for _ in range(100)]

    correctanswers = [sum(sublist) for sublist in outcomes]
    correctanswers = sorted(correctanswers)
    estimatedskills = [-3 + (6/99)*i for i in range(100)]
    
    answeredcorrectly = [sum([sublist[i] for sublist in outcomes]) for i in range(len(outcomes))]
    answeredcorrectly = sorted(correctanswers)
    estimateddifficulties = [-3 + (6/99)*i for i in range(100)]

    simulatedcorrectanswers = []
    for p in range(100):
        est = 0
        for i in range(100):
            diff = estimatedskills[p] - estimateddifficulties[i]
            est += sigm(diff)
        simulatedcorrectanswers.append(est)

    anomalies = [correctanswers[i] - simulatedcorrectanswers[i] for i in range(100)]
    susp = anomalies.index(max(anomalies)) + 1
    print("Case #{}: {}".format(case, susp))