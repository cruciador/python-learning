## python dictionary type

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

## Python Set Data Type

set1 = {2023, "Python", 3.11, 5+6j, 1.23E-4}
print(set1)              # Prints the set
print(type(set1))        # <class 'set'>
print(2000 in set1)  # Checks if 2000 is in the set
print("Python" in set1)  # Checks if "Python" is in the set

# Iterate through set
print("Items in set:")
for item in set1:
    print(item)

# Iterate through set in sorted order
print("Items in sorted order (excluding complex numbers):")
for item in sorted((x for x in set1 if not isinstance(x, complex)), key=str):
    print(item)


# Declaring a variable
# And, assigning a Null value (None)

x = None

# Printing its value and type
print("x = ", x)
print("type of x = ", type(x))

# dictionary example
dict_example = {
    "name": "Alice",
    "age": 30,
    "is_student": False,
    "courses": ["Math", "Science"],
    "address": {
        "city": "Wonderland",
        "zip": "12345"
    }
}
print("Dictionary Example:")
print(dict_example)
print(dict_example["name"])