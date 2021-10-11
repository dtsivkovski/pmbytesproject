#Activity 1

student_list = ['pam', 'rob', 'joe', 'greg', 'bob', 'amy', 'matt']
print(student_list[2:5])
print(student_list[:-5])
print(student_list[0:6])

if 'rob' in student_list:
    print('Yes, Rob is on the student list')
else:
    print('No, Rob is not on the student list')

#Activity 2

p1 = { "name":"John", "age":61, "city":"Eugene"}
p2 = { "name":"Risa", "age":16, "city":"New York"}
p3 = { "name":"Ryan", "age":16, "city":"Los Angeles"}
p4 = { "name":"Shekar", "age":16, "city":"San Francisco"}
# a list of dictionaries
list_of_people = [p1, p2, p3, p4]
# write some code to Print List of people one by one