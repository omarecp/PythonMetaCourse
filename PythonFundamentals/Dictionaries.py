from random import sample
from shutil import SameFileError


sampleDictionary = {1: 'Coffe',2: "Tea", 3: "Juice"}
sampleDictionary[2]= "Mint Tea"

print(sampleDictionary[1])

sampleDictionary[4] = "Beer"

print(sampleDictionary[4])


del sampleDictionary [4]

for key,value in sampleDictionary.items():
    print(str(key) + ": " + str(value))