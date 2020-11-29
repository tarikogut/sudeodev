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