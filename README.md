# sudeodev

YBS405. Assignment 2 
Due Date: December 04, 2020 at 23:55
1.	Create a list of lists in which each element in a list appears with the number of repetitions. Example input: [1,2,3,1,2,1,4,5,3]
Example output: [[1,3], [2,2], [3,2], [4,1], [5,1]]

Solution:
myList = [1,2,3,1,2,1,4,5,3]
output=[]

for i in set(myList):
  c = myList.count(i)
  output.append([i,c])
print(output)
2.	Definition: The element of a list can be an empty list, a number, or a list.
The following examples conform to the above definition:
Exampled: [1,2,3,4]
Example2: []
Example 3: [[1,2], 2, [3,4]]
Example 4: [[[1], [2]], [1], [3,3,4], 5]
Take a list that conforms to the definition above and produce a flat list. The outputs for the above examples are as follows:
Output 1: [1,2,3,4]
Output 2: []
Output 3: [1,2,2,3,4]
Output 4: [1,2,1,3,3,4,5]

Solution:





def flatten_list(liste):
    if len(liste) == 0:
        return liste
    if isinstance(liste[0], list):
        return flatten_list(liste[0]) + flatten_list(liste[1:])
    return liste[:1] + flatten_list(liste[1:])

exampleone = flatten_list([1,2,3,4])
exampletwo = flatten_list([])
examplethree = flatten_list([[1,2], 2, [3,4]])
examplefour = flatten_list([[[1], [2]], [1], [3,3,4], 5])

print(exampleone)
print(exampletwo)
print(examplethree)
print(examplefour)

3.	Write a code that take the two sets and generate their intersectsions  Example Input: s1 = {1,2,3}, s2 = {a, b, 1,2}
intersection (s1, s2) -> {1,2}

Solution:
s1 = {1,2,3}
s2 = {"a", "b", 1,2}
print(s1&s2)
print(s1.intersection(s2))

4.	Write the function that keeps the permutations of the elements of a given list in the sub-lists. Example Input: [1,2,3]
Example Output: [[1,2,3], [2,3,1], [3,1,2], [1,3,2], [2,1,3], [3,2,1] ]]
Note: it does not have to come out in the same order as original list.



from itertools import permutations
inputlist = [1,2,3]
output = []
perm = permutations(inputlist)
for i in list(perm):
  output.append(list(i))
print(output)

5.	Write the code that extracts all subsets of a given set into a list: Example Input: {1,2,3}
Example Output: [{}, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}]

Solution:

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

6.	Write the code that removes repetitive elements in a list Example input: [1,2,3,1,2,1,3,4]
Example output: [1,2,3,4]
Solution:
inputList = [1,2,3,1,2,1,3,4]
output = sorted(set(inputList))
print(output)
