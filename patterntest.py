import re
pattern = re.compile('add device \d+\:')
match = pattern.match('add device 10: /dev/input/event0\n: /dev/input/event9\n')
print(match.group())
print('add device 1:'.replace('add device \d:',''))