str1 = str(2.3) # Type casting float to string
print("Type of str1:", type(str1))  # <class 'str'>

str2 = str(100)  # Type casting int to string
print("Type of str2:", type(str2))  # <class 'str'>

str3 = str(True)  # Type casting bool to string
print("Type of str3:", type(str3))  # <class 'str'>

int1 = int(2.3)  # Type casting float to int
print("Type of int1:", type(int1))  # <class 'int'>
int2 = int("100")  # Type casting string to int
print("Type of int2:", type(int2))  # <class 'int'>

int3 = int(True)  # Type casting bool to int
print("Type of int3:", type(int3))  # <class 'int'>
print("int3 value:", int3)  # Output: 1


# Converting a binary string to an integer
binary_str = "1010"
int_value = int(binary_str, 2)
print(int_value)

