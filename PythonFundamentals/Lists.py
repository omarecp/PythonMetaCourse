listOne  = [1,2,3,4,5]
listTwo = ['A','B','C']
listThree = ['Hello',1,True,40.22]

print(*listOne) 



listOne.append(6)

##listOne.extend(7,8,9)

listOne.pop(4)

del listOne[2]

print(listOne,sep = " ")

for item in listOne:
    print("Value: " ,item)