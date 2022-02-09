## left side key, right side value
phonebook = {"Chris": "555−1111", "Katie": "555−2222", "Joanne": "555−3333"}


print()
print("*****  start section 1 - print dictionary ********")
print()


print(phonebook)
print(type(phonebook))

phone = phonebook["Chris"]

print(phone)
'''
print(len(phonebook))


print()
print("*****  end section 1 ********")
print()





print()
print("*****  start section 2 - search dictionary ********")
print()


name = "chris"

if name in phonebook:
    print(phonebook[name])
else:
    print(name, "is not in the phonebook")


print()
print("*****  end section 2 ********")
print()



print()
print("*****  start section 3 - edit/append dictionary ********")
print()

## list - immutable
## tuple - mutable

phonebook["chris"] = "555-0123"
phonebook["Chris"] = "555-4444"
print(phonebook)

print()
print("*****  end section 3 ********")
print()



print()
print("*****  start section 4 - delete/remove from dictionary ********")
print()

del phonebook["Chris"]

print(phonebook)

print()
print("*****  end section 4 ********")
print()



print()
print("*****  start section 5 - iterate through keys ********")
print()

for k in phonebook:
    print(k)
    print(phonebook[k])

print()
print("*****  end section 5 ********")
print()


print()
print("*****  start section 6 - iterate through values  ********")
print()

for value in phonebook.values():
    print(value)

print()
print("*****  end section 6 ********")
print()


print()
print("*****  start section 7 - iterate through both key and value pair********")
print()

for phonebook_tuple in phonebook.items():
    print(phonebook_tuple)

for key, value in phonebook.items():
    print(key)
    print(value)

print()
print("*****  end section 7 ********")
print()



print("***** start section 8 - using get and clear ******")

phone = phonebook.get("chris", "key not found")
print(phone)

phonebook.clear()
print(phonebook)

print("****** end section 8 *****")


print("**** start section 9 - using pop method *******")

remove = phonebook.pop("Chris", "not found")
print(remove)

print(phonebook)



print('**** end section 9 ******')


print("***** start section 10 - using popitem *******")

a = phonebook.popitem()

print(a)
print(phonebook)

print("**** end section 10 *****")

"""
import random

print()
print("*****  start section 11 - using random and converting to list ********")
print()

# list_of_keys = list(phonebook)
# random_key = random.choice(list_of_keys)
# phone = phonebook[random_key]

phone = phonebook[random.choice(list(phonebook))]

print(phone)

print()
print("*****  end section 11 ********")
print()
'''
