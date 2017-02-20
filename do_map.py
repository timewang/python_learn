
def normalize(s) :
    s = s.lower()
    s = s.capitalize()
    print(s)
    return s



L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)