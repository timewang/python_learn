import re

results = [];

with open('input_file.txt', 'rt') as f:
    index = -1
    for line in f:
        index = index+1
        results.append(line)
        if line.startswith("could not"):
            print('前两行不要')
            results.pop(index)
            results.pop(index - 1)
            results.pop(index - 2)
            index = index - 3

print(results)
for s in results:
    if not s.startswith("add device"):
        results.remove(s)
print(results)
results2 = []
for s1 in results:
    pattern = re.compile('add device \d+\:')
    match = pattern.match(s1)
    if match:
        print(match.group())
        results2.append(s1.replace(match.group(), ''))

print(results2)
print(results2[0])




