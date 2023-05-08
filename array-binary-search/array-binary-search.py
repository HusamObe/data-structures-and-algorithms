def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

 
# Test arrays
arr = [4, 8, 15, 16, 23, 42]
x = 15
print("array 1",binary_search(arr, x))

arr = [-131, -82, 0, 27, 42, 68, 179]
x = 42
print("array 2",binary_search(arr, x))

arr = [11, 22, 33, 44, 55, 66, 77]
x = 90
print("array 3",binary_search(arr, x))

arr = [1, 2, 3, 5, 6, 7]
x = 4
print("array 4",binary_search(arr, x))