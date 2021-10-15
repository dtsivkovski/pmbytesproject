import json

print(' Challenge 1 ')

student_list = ['Pam', 'Rob', 'Joe', 'Greg', 'Bob', 'Amy', 'Matt']
print(student_list[2:5])
print(student_list[5:6])
print(student_list[0:6])

if 'Rob' in student_list:
    print("Yes, Rob is in the student list.")
else:
    print("No, Rob is not in the student list.")

print(' ')
print(' Challenge 2 ')

p1 = {"name": "John", "age": 61, "city": "Eugene"}
p2 = {"name": "Risa", "age": 16, "city": "New York"}
p3 = {"name": "Ryan", "age": 16, "city": "Los Angeles"}
p4 = {"name": "Shekar", "age": 16, "city": "San Francisco"}
# a list of dictionaries
list_of_people = [p1, p2, p3, p4]
# write some code to Print List of people one by one (SEE BELOW)
for i in list_of_people:
    print(i['name'])

print(" ")

# turn list to dictionary of people
dict_people = {'people': list_of_people}
print("List to Dictionary of people")
print(type(dict_people))
# print(dict_people)
# write some code to Print People from Dictionary (SEE BELOW)
print(" ")
print("Names of people:")
for i in dict_people['people']:
    print(i['name'])

print(" ")

# Creating a json dump
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