n = int(input())
x0, y0, xhole, yhole = [int(x) for x in input().split()]

movedict = {(0, 1): "up", (0, -1): "down", (1, 0): "right", (-1, 0): "left"}

def move(d, scooters, robot):
    print(movedict[d])
    robot[0] += d[0]
    robot[1] += d[1]
    cx = robot[0]
    cy = robot[1]
    flag = False
    while (cx, cy) in scooters:
        flag = True
        cx += d[0]
        cy += d[1]
    if flag:
        scooters.remove(tuple(robot))
    if (cx, cy) != (xhole, yhole):
        scooters.append((cx, cy))
    return scooters, robot

robot = [x0, y0]

scooters = []

for _ in range(n):
    scooters.append(tuple(int(x) for x in input().split()))

while scooters:
    scooterx, scootery = scooters[0]
    if scooterx == robot[0]:
        scooters, robot = move((1, 0), scooters, robot)
        if scootery > yhole:
            while robot[1] != scootery + 1:
                if robot[1] > scootery:
                    scooters, robot = move((0, -1), scooters, robot)
                elif robot[1] <= scootery:
                    scooters, robot = move((0, 1), scooters, robot)
        else:
            while robot[1] != scootery - 1:
                if robot[1] >= scootery:
                    scooters, robot = move((0, -1), scooters, robot)
                elif robot[1] < scootery:
                    scooters, robot = move((0, 1), scooters, robot)
        while robot[0] != scooterx:
            scooters, robot = move((1 if robot[0] < scooterx else -1, 0), scooters, robot)
        if robot[1] < scootery:
            while robot[1] != yhole - 1:
                scooters, robot = move((0, 1), scooters, robot)
        if robot[1] > scootery:
            while robot[1] != yhole + 1:
                scooters, robot = move((0, -1), scooters, robot)
    
    if robot[0] == xhole:
        continue
    elif robot[0] > xhole:
        scooters, robot = move((1, 0), scooters, robot)
    else:
        scooters, robot = move((-1, 0), scooters, robot)
    
    if robot[1] == yhole:
        continue
    elif robot[1] > yhole:
        scooters, robot = move((0, -1), scooters, robot)
    else:
        scooters, robot = move((0, 1), scooters, robot)
    
    if robot[0] > xhole:
        while robot[0] != xhole + 1:
            scooters, robot = move((-1, 0), scooters, robot)
    else:
        while robot[0] != xhole - 1:
            scooters, robot = move((1, 0), scooters, robot)