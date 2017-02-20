def is_palindrome(n):
    snum = str(n)
    lehgth = len(snum)
    if lehgth < 3:
        return False
    rsnum = ''
    for c in range(0,lehgth):
        rsnum += snum[lehgth - (c + 1)]
    return snum == rsnum



output = filter(is_palindrome, range(1, 2000))
print(list(output))