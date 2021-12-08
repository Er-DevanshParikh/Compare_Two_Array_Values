# Task : Write a program to print common elements from two arrays.
# Declare an empty two arrays
a = []
b = []

# Getting Values from User...
array1 = int(input("Enter value of Array 1 :"))
for i in range(0, array1):
    value_a1 = int(input())
    a.append(value_a1)
array2 = int(input("Enter value of Array 1 :"))
for j in range(0, array2):
    value_a2=int(input())
    b.append(value_a2)
# Print the array value total number of length
n1 = len(a)
n2 = len(b)
print("Length of First Array :", +n1)
print("Length of Second Array :", +n2)
print("Common elements Are :")
# check the value starting from 0
# Until the total size of arrays
i = 0
j = 0
while i < n1 and j < n2:
    # Compare the array1 value with array2 and increment the value of j
    if a[i] == b[j]:
        print(a[i])
        i += 1  # i=i+1
        j += 1  # j=j+1

    # a < b
    elif a[i] < b[j]:
        i += 1  # i=i+1

    else:
        j += 1  # j=j+1




