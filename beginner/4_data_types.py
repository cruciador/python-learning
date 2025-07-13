## 1. Remember, number objects are created when you assign a value to a variable.

var1 = 1       # int data type
var2 = True    # bool data type
var3 = 10.023  # float data type
var4 = 10+3j   # complex data type

print(type(var4)) # <class 'complex'>

# 2. String data type

str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string

# 3. Example of List Data Type

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']


print (list)          # Prints complete list
print (list[0])       # Prints first element of the list
print (list[1:3])     # Prints elements starting from 2nd to
print (list[2:])      # Prints elements starting from 3rd element
print (tinylist * 2)  # Prints list two times
print (list + tinylist) # Prints concatenated lists

# 4. Range Data Type: range(start, stop, step)

for i in range(5):
  print(i)

for i in range(2, 5):
  print(i)

for i in range(1, 5, 2):
  print(i)

# 5. Bytes Data Type
b1 = bytes([65, 66, 67, 68, 69])  
print(b1)

