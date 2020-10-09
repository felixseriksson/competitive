rows, columns = [int(x) for x in input().split()]
wall = []
wall.append(input().split())
for row in range(rows):
    wall.append([int(x) for x in input().split()])
wall.append(input().split())

energyrec = list(wall)
energyrec[0] = [0 for i in range(columns)]
energyrec[1] = [0 for i in range(columns)]
for row in range(2, rows):
    for col in range(columns):
        fromthisnode = 
        energyrec[row][col] = min()