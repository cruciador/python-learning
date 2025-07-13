n = 7

first = 0
second = 1
print(first, end =", ")
print(second, end =", ")
for i in range(n-2):
    sum = first + second
    if (i == n-3) :
        print(sum)
    else :
        print(sum, end =", ")
    first = second
    second = sum

