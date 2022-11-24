num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]
##1.Under the num_list create a new for loop and print out each value on the list in sequential order.
print("Exercise 1")
for item in num_list:
     print(item)
##2.  Inside the for loop, create a condition that will look for all numbers that are greater than 45 and print out only numbers that meet that condition
print("Exercise 2")
for item in num_list:
    if item > 45:
     print(item)
##3.  Change the print statement to “Over 45” and add an else condition with a print statement of “Under 45”.
print("Exercise 3")
for item in num_list:
    if item > 45:
     print(item,"Over 45")
    else:
        print(item,"Under 45")
##4.  Update the for loop to use the enumerate function so you can get and use the index. Alter the condition to look for number 36 and print out the following: ‘Number found at position: ‘, index number
print("Exercise 4")
for position ,item in enumerate(num_list):
    if item == 36:
        print("Number found at position:",position,item)
##5.  Next, create a new variable called count and assign it a value of 0 and place it outside the for loop.
count = 0
print("Exercise 5")
for position ,item in enumerate(num_list):
    if item == 36:
        print("Number found at position:",position,item)
##6,7,8Inside the for loop increment the counter by 1. Add a print statement outside the for loop to print the value of the count variable.
##Finally, add a break statement directly after the print statement inside the if condition for finding the number. 
print("Exercise 6")
for position ,item in enumerate(num_list):
    if item == 36:
        print("Number found at position:",position,item)
        break
    count+=1
print(count)