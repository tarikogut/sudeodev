import itertools
inputlist = {1,2,3}
output = []
for L in range(0, len(inputlist)+1):
    for subset in itertools.combinations(list(inputlist), L):
        if subset is None:
          output.append({})
        else:
          output.append(set(subset))
print(output)