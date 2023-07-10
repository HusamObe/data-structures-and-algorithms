def Insert(sorted_array, value):
    i = 0
    while i < len(sorted_array) and value > sorted_array[i]:
        i = i + 1
    while i < len(sorted_array):
        temp = sorted_array[i]
        sorted_array[i] = value
        value = temp
        i = i + 1
    sorted_array.append(value)


def InsertionSort(input_array):
    sorted_array = []
    sorted_array.append(input_array[0])

    for i in range(1, len(input_array)):
        Insert(sorted_array, input_array[i])

    return sorted_array


arr = [8, 4, 23, 42, 16, 15]
sorted_arr = InsertionSort(arr)
print(sorted_arr)
