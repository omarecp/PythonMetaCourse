#bill = 175.00
#taxRate = 15
#totalTax =(bill * taxRate)/100
#print("Total tax",totalTax)

def calculateTax(bill,taxRate):
    return round((bill*taxRate)/100,2)

print("Total Tax",calculateTax(175.00,15))
print("Total Tax",calculateTax(164.33,22))