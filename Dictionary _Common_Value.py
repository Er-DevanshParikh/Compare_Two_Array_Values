def common_element_dict(array1, array2):
    # empty dictionary
    dict1 = {}
    for elements in array2:
        dict1[elements] = 1

    count = 0
    for i in array1:
        if dict1.get(i) is not None:
            print(i)
            count = count + 1


a1 = [1, 2, 3]
a2 = [3, 4, 5]
common_element_dict(a1, a2)
