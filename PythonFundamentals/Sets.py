from os import set_blocking


setA = {1,2,3,4,5}
setA.add(6)
print(setA)


setA.discard(2)
print(setA)

setB = {7,8,9}
setC = {8,9,10}

print(setA.union(setB))
print(setB.intersection(setC))
print(setB.difference(setC))
