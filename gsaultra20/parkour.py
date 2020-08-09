def solution(ps):
    ps = [sorted(i) for i in ps]
    # height, speed, time
    times = [[[i, 5, 5] for i in ps[0]]] + [[None]*len(ps[0])]*(len(ps)-1)
    for index in range(1, len(ps)):
        for platformindex in range(len(ps[index])):
            speed = "a"
            time = "b"
            times[index][platformindex] = [ps[index][platformindex], speed, time]
    return times

print(solution([(1, 2, 3), (1, 2, 3), (1, 2, 3), (1, 2, 3), (1, 2, 3)]))