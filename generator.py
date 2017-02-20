

def triangles():
    t = 0
    last = []
    tri = [1]
    while True:
        if t == 0:
            yield tri
            last = tri
            t = 1
            tri = list(range(2))
        elif t == 1:
            for index in tri:
                tri[0] = 1
                tri[1] = 1
            yield tri
            last = tri
            t = 2
            tri = list(range(3))
        else:
            for index in tri:
                if index == 0:
                    tri[index] = 1
                    continue
                if index == len(tri) - 1:
                    tri[index] = 1
                    continue
                else:
                    tri[index] = last[index] + last[index - 1]
            yield tri
            last = tri
            t = t + 1
            tri = list(range(t + 1))
        #return 'done'

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break