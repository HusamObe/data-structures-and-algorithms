#inserting element in the middle of the array
def insertShiftArray(arr,value):
    # print (arr,value)
    middle= len(arr)//2
    #print (middle)
    new_arr = []
    for i in range(len(arr)):
        if i == middle:
            new_arr.append(value)
        new_arr.append(arr[i])
    return new_arr

# remove element from the middle array
def removeElement(arr):
    middle = len(arr)//2
    for i in range(middle,len(arr)-1):
        arr[i] = arr[i+1]
    arr.pop()
    return arr


arr = [2,4,6,-8]
x = 5
new_arr1 = insertShiftArray(arr, x)
print(new_arr1)
rm_arr = removeElement(new_arr1)
print(rm_arr)


arr = [42,8,15,23,42]
x = 16
new_arr1 = insertShiftArray(arr, x)
print(new_arr1)
rm_arr = removeElement(new_arr1)
print(rm_arr)