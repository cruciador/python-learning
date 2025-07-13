x = 10
y = 20

print ("not (x+y>15):", not (x+y)>15)

'''Logical Operators To Compare Sequences (Lists)
Finally, two list objects below are non-empty. Hence x and y returns the latter, and x or y returns the former.'''

x=[1,2,3]
y=[10,20,30]

print("x  and  y: ", x and y)

print("x  or  y:", x or y)

# Logical operations with non boolean conditions
x = 10
y = 20
z = 0
print("x and y:",x and y)
print("x or y:",x or y)
print("z or x:",z or x)
print("y or z:", y or z)