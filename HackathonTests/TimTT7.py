#Activity 1
student_list = ['pam','rob','joe','greg','bob','amy','matt']
print(' ')
#The following print statement includes elements at index 2 & excludes element at index 5
print(student_list[2:5])
print(' ')
#print elements beginning to 4th
print(student_list[:-5])
print(' ')
#print elements 6th to end(index 5)
print(student_list[5:])
print(' ')
#print elements beginning to end
print(student_list)
print(' ')
#check if rob is in the student_list
if 'rob' in student_list:
    print("rob is in the student_list")
else:
    print("rob is not in student_list")