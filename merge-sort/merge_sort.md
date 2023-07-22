# Merge Sort Algorithm

Merge Sort is a popular sorting algorithm known for its efficiency and stability. It follows the divide-and-conquer approach to divide the input array into smaller subarrays, sort them individually, and then merge them back together to produce a sorted array. In this article, we will explore the step-by-step process of Merge Sort and provide a Python implementation.

## Algorithm Overview

The Merge Sort algorithm can be summarized in the following steps:

1. Split the input array into two halves.
2. Recursively sort the left and right halves.
3. Merge the sorted halves back together.

## Pseudocode

```css
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```


## Step-by-Step Walkthrough

To demonstrate the Merge Sort algorithm, let's use the sample array `[8, 4, 23, 42, 16, 15]` and go through each step of the sorting process.

1. Initial state: `[8, 4, 23, 42, 16, 15]`
2. Split the array into two halves:
   - Left side: `[8, 4, 23]`
   - Right side: `[42, 16, 15]`
3. Recursively sort the left side: `[4, 8, 23]`
4. Recursively sort the right side: `[15, 16, 42]`
5. Merge the sorted left and right sides together:
   - Comparing the elements: `[4, 8, 23]` and `[15, 16, 42]`
   - Merging the elements: `[4, 8, 15, 16, 23, 42]`

## Python Implementation

Here's a working implementation of Merge Sort in Python:

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


arr = [8, 4, 23, 42, 16, 15]
merge_sort(arr)
print(arr)
```

## Conclusion

* Merge Sort is an efficient and stable sorting algorithm with a time complexity of O(n log n). It divides the input array into smaller subarrays, recursively sorts them, and then merges them back together to produce a sorted array. Merge Sort's divide-and-conquer approach makes it suitable for handling large data sets.