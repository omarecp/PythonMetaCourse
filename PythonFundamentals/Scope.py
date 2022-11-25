myGlobal = 10
def functionOne():

    enclosedVariable = 8

    def functionTwo():
        localVariable = 5
        print("Acces to global",myGlobal)
        print("Acces to enclosed",enclosedVariable)
    functionTwo()
functionOne()
    