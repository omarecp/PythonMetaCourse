def sumOf(**kwargs):
    sum = 0
    for key,value in kwargs.items():
        sum += value
    return sum

print(sumOf(coffe=2.99,cake = 4.55, juice = 3.60))