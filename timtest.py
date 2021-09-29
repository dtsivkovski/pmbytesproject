# Challenge 1: Name the variable types of the following variables. Print them out into console in the format "Variable: Variable Type" (might have to google "how to print variables in python")
var1 = 3
var2 = "Mr. Mortensen"
var3 = 'f'
var4 = 0.4

print(var1, 'is a integer')
print(var2, 'is a string')
print(var3, 'is a string')
print(var4, 'is a float')

print(' ')
# Challenge 2: Pass list1 into list2. However, list2 must contain the elements of list1 in order. Print list2. +0.3 if you can create a function to order a list and can display it on your website
list1 = [5, 3, 4, 1, 2]
list2 = [list1[3], list1[4], list1[1], list1[2], list1[0]]

print(list1, "ordered is",  list2)

print(' ')
# Challenge 3: Find a way to add 3 to each element in the array. Then, take the average of the array and put it into the variable avg. +0.2 if you can turn this into a function and display it on your website.
averageList = [23, 41, 90, 55, 71, 83]
averageList2 = [x+3 for x in averageList]
avg = [sum(averageList2)/len(averageList2)]
print(averageList2, "adds 3 to averageList")
print(avg, "is the average of averageList + 3")