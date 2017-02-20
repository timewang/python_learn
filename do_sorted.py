from operator import itemgetter

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    print(t[0])
    #t[0].lower
    return t[0]


L2 = sorted(L, key=by_name)
print(L2)

def by_score(t):
    return int(t[1])


L4 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

L3 = sorted(L4, key=by_score)
print(L3)

print(sorted(L4 , key=itemgetter(0)))
print(sorted(L4 , key=lambda t: t[1]))
print(sorted(L4 , key=itemgetter(1), reverse=True))