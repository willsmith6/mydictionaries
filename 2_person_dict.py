person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)
print('\n')

print(type(person['children']))
print('\n')

print(person['children'][1])
print('\n')

print(person["pets"]["cat"])
print('\n')

for i in person['children']:
    print(i)

for i in person['pets']:
    print(person['pets'][i])

print('\n')


for i in person['pets'].values():
    print(i)