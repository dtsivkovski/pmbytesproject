import json

print('Activity 1')
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

print(' ')
print('Activity 2')
print(' ')
p1 = { "name":"John", "age":61, "city":"Eugene"}
p2 = { "name":"Risa", "age":16, "city":"New York"}
p3 = { "name":"Ryan", "age":16, "city":"Los Angeles"}
p4 = { "name":"Shekar", "age":16, "city":"San Francisco"}
# a list of dictionaries
list_of_people = [p1, p2, p3, p4]
# write some code to Print List of people one by one

for i in list_of_people:
    print(i['name'])

print(' ')

# turn list to dictionary of people
dict_people = {'people': list_of_people}
print("List to Dictionary of people")
print(type(dict_people))
# write some code to Print People from Dictionary

for i in dict_people['people']:
    print(i['name'])

print(' ')

# turn dictionary to JSON
print(" - Dumps - Python to JSON String - ")
json_people = json.dumps(list_of_people)
print(type(json_people))
json_dict = json.loads(json_people)
# to list
names = [person['name'] for person in json_dict]
print("Names of people to list: " + str(names))
print(" ")
print("Names of people: ")
# pretty print Names of People (SEE BELOW)
for name in names:
    print(name)