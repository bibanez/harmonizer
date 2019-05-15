import numpy as np
from itertools import product

test_list = [[[3, 2], [2, 3]], [[2, 1], [1, 2]]]
test_list_2 = [3, 2, 4]
test_list_3 = [2, 4, 6, 7]
final_list = []

for x in test_list_2:
    for y in test_list_3:
        final_list += [[x, y]]

print(final_list)

numpy_array = np.array([[[2,3], [4, 5], [6, 5], [7, 8]], [[3, 4], [5, 2], [8, 16], [1, 12]]])

for x in range(numpy_array.shape[0]):
    for y in range(numpy_array.shape[1]):
        print(numpy_array[x, y, :])

print("")

def combination(list1, list2):
    list = []
    for x in list1:
        for y in list2:
            list.append([x, y])
    return list

print(combination(test_list_2, test_list_3))

for a in product(test_list_2, test_list_3):
    print(a)
