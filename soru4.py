from itertools import permutations
inputlist = [1,2,3]
output = []
perm = permutations(inputlist)
for i in list(perm):
  output.append(list(i))
print(output)