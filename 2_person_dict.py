person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
#int is the object
person["spouse"] = "Edna"
#string is the object
person["children"] = ["Ralph", "Betty", "Joey"]
#list is the object
person["pets"] = {"dog": "Fido", "cat": "Sox"}
#dictionary is the object


print(person)

# print out the name of the second child
children = person["children"]

print(type(children)) #tells you type of variable, tells you children is a list
print(children[1]) #how Bhojwani did it
print(person["children"][1]) # how I did it, preferable bc no variables

# print out the name of the cat
pets = person["pets"]

print(type(pets))

print(pets["cat"])

print(person["pets"]["cat"])
#instead of index value, use the key



# use a loop to print out the names of each child
for child in person["children"]:
    print(child)


# use a loop to print out the pets in the following format:
# The type of pet is: dog and the name of the pet is: Fido

for k,v in person["pets"].items(): #k,v means key and value
    print(f"The type of pet is: {k} and the name of the pet is: {v}")