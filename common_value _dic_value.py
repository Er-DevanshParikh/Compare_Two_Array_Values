# Create an empty dictionary..
array1 = {}
array2 = {}
n = int(input("Number of elements :"))
# Create array from first string values
print("Enter Elements for Array 1:[Key:Value]")
for i in range(n):
    b = input("Enter Key:")
    c = input("Enter Value:")
    array1.update({b:c})
# Create array from second string values
print("Enter Elements for Array 2:[Key:Value]")
for i in range(n):
    m = input("Enter Key:")
    n = input("Enter Value:")
    array2.update({m:n})

print(array1)
print(array2)
# Find common elements
common = list(set(array1.values()).intersection(set(array2.values())))
common.sort()
print(common)
