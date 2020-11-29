myList = [1,2,3,1,2,1,4,5,3]
output=[]

for i in set(myList):
  c = myList.count(i)
  output.append([i,c])
print(output)