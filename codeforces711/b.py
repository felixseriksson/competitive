from collections import defaultdict
for _ in range(int(input())):
    nboxes, containerwidth = [int(x) for x in input().split()]
    b = ([int(x) for x in input().split()])
    boxes = defaultdict(int)
    for item in b:
        boxes[item] += 1
    # binarycontainerwidth =  str(bin(containerwidth))[2:]
    # print(binarycontainerwidth)
    keys = sorted(boxes.keys(), reverse=True)
    height = 0
    while sum(boxes.values()) > 0:
        width = containerwidth
        height += 1
        for key in keys:
            if boxes[key]:
                n = min(boxes[key], width//key)
                boxes[key] -= n
                width -= key*n
            else:
                continue
            if width == 0:
                break
    print(height)