def sumOf(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(sumOf(4,5,6))