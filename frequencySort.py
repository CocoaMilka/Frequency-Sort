from pprint import pprint

class Node:

    frequency = 0
    value = 0

    def __init__(self, f, v):
        self.frequency = f
        self.value = v

def findMax(A):
    max = 0
    for i in A:
        if i > max:
            max = i
    return max

# Quick Sort Functions
def Partition(A, p, r):
    x = A[r].frequency
    i = p - 1

    for j in range(p, r):
        if A[j].frequency >= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]

    return i + 1

def QuickSort(A, p, r):
    if p < r:
        q = Partition(A, p, r)
        QuickSort(A, p, q - 1)
        QuickSort(A, q + 1, r)


# test_array = [3, 5, 2, 1, 0, 1, 2, 3, 4, 2, 0, 3, 4, 2, 1]
test_array = [99, 99, 99, 5, 5, 5, 1, 101, 1, 1, 3, 3, 3, 8, 101, 8, 8, 4, 4, 4, 4, 101]

print("Max element: ",findMax(test_array))

sorted_array = []

frequency = [0] * (findMax(test_array) + 1)

node_array = []

# Value at index is how many times each index number appears
for i in test_array:
    frequency[i] += 1

# Populate node array with frequency:value
for i in range(0, len(frequency)):
    if frequency[i] != 0:
        node_array.append(Node(frequency[i], i))

# Sort array by frequencies
QuickSort(node_array, 0, len(node_array) - 1)

# Populate sorted array
for i in node_array:
    for j in range(0, i.frequency):
        sorted_array.append(i.value)

pprint(sorted_array)


'''
for i in node_array:
    print("Value: ", i.value)
    print("Frequency: ", i.frequency)
'''
