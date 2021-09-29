var1 = 3
var2 = "Mr. Mortensen"
var3 = 'f'
var4 = 0.4

print(var1, 'is a integer')
print(var2, 'is a string')
print(var3, 'is a string')
print(var4, 'is a float')

print(' ')

list1 = [5, 3, 4, 1, 2]
list2 = [list1[3], list1[4], list1[1], list1[2], list1[0]]

print(list1, "ordered is",  list2)

print(' ')

averageList = [23, 41, 90, 55, 71, 83]
averageList2 = [x+3 for x in averageList]
avg = [sum(averageList2)/len(averageList2)]
print(averageList2, "adds 3 to averageList")
print(avg, "is the average of averageList + 3")