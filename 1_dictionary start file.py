import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}
#dictionary is called phonebook, 3 key value pairs. Left side is key, right side is value
#commas indicate another key-value pair follows



print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)
print(len(phonebook))
#gives length and gives a '3', this is because it counts key-value elements. There are 3.

mydictionary = {}
#creates empty dictionary
print(mydictionary)

mydictionary = dict(m=8, n=9)
#also creates empty dictionary using dict function
#m and n are the key value pair. key is m, value is 8. key is also n, value is 9.
print(mydictionary)

phone = phonebook['chris']
#how to access values in dictionary, give it a key
#if make 'Chris' into lower case 'chris', gives key error bc cannot find that key in dictionary. make sure it matches key exactly
print(phone)

print()
print('*****  end section 1 ********')
print()



print()
print('*****  start section 2 - search dictionary ********')
print()

name = 'Chris'

#v will search through all keys in phonebook
if name in phonebook:
    print(f"{name} has the phone number: {phonebook[name]}")
    #put phonebook[name] bc it represents Chris
else:
    print(f"{name} not found")


print()
print('*****  end section 2 ********')
print()


print()
print('*****  start section 3 - edit/append dictionary ********')
print()

#cannot edit key, can delete key-value pair but cannot edit just the key
print(phonebook)
phonebook['Joe'] = '555-0123' #appends Joe to phonebook
phonebook['Chris'] = '555-4444' #updates Chris's phone number
print(phonebook)
del phonebook['Chris'] #deletes entire Chris key-value pair from phonebook
print(phonebook)


print()
print('*****  end section 3 ********')
print()





print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()




print()
print('*****  end section 4 ********')
print()


print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()


for k in phonebook:
    print(f"the key is {k} and the value is {phonebook[k]}")
    #the k object is a string

for v in phonebook.values():
    print(v)
    #.values is a method of dictionaries, allows you to iterate thru all values of dictionary

for phone_tuple in phonebook.items():
    print(phone_tuple)
    #.items gives both key and value together in a tuple

for k,v in phonebook.items():
    print(f"the key is {k} and the value is {v}")
    #can seperate key and value into 2 seperate elements




print()
print('*****  end section 5 ********')
print()


print()
print('*****  start section 6 - using get and clear ********')
print()

#.get method helps avoid lowercase chris error. Gives us a None variable instead of null when no match. can give alt arguement
phone = phonebook.get('Jack', '911')
print(phone)
#so now 911 shows up for Jack since he is not in the dictionary

phonebook.clear() #clears out dictionary
print(phonebook)



print()
print('*****  end section 6 ********')
print()


print()
print('*****  start section 7 - using pop method ********')
print()


#allows you to pop a key and value out of dictionary
print(phonebook)
phone = phonebook.pop('Katie')
print(phone)
print(phonebook)
#originally have Katie included in dictionary, but after she has been removed from dictionary


print()
print('*****  end section 7 ********')
print()


print()
print('*****  start section 8 - using popitem ********')
print()

#.popitem was supposed to let you randomly select value of dictionary, but randomness does not work for some reason

phone = phonebook.popitem()
print(phone)
print(phonebook)
#supposed to be random, but it keeps giving Joanne bc she's last

#in order to do random value in list, do .randomitem
#in order to do a true random value in dictionary




print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using random and converting to list ********')
print()

#how to workaround .popitem not working and do a random selection of dictionary:

list_of_keys = list(phonebook)
print(list_of_keys)
#turns dictionary into a list of keys

random_key = random.choice(list_of_keys)
print(random_key)
#prints random key

print(phonebook[random_key])
#prints random phonenumber

#how to do it all in one line vvvv
print(phonebook[random.choice(list(phonebook))])



print()
print('*****  end section 9 ********')
print()





