# Insertion Sort Algorithm

* Insertion Sort is a simple sorting algorithm that divide an array into two parts: a sorted subarray and unsorted subarray.

* algorithim iterates the unsorted subarray,it start to compare each element in the unsorted array with the elements in the sorted one and insert it into its correct position. Until the entire array are sorted.

----
## The Pseudocode

```css
Insert(int[] sorted, int value)
  initialize i to 0
  WHILE value > sorted[i]
    set i to i + 1
  WHILE i < sorted.length
    set temp to sorted[i]
    set sorted[i] to value
    set value to temp
    set i to i + 1
  append value to sorted

InsertionSort(int[] input)
  LET sorted = New Empty Array
  sorted[0] = input[0]
  FOR i from 1 up to input.length
    Insert(sorted, input[i])
  return sorted
```

* This pusedo has two functions **Insert** and **InsertionSort**

* The **Insert** function takes a sorted array **(sorted)** and a value **(value)** and inserts the value into the correct position in the sorted array. 

* The **InsertionSort** function takes an input array and sorts it using the **Insert** function.

---

## Step-by-Step Walkthrough

> sample array [8, 4, 23, 42, 16, 15].


<ol>
<li>Init empty sorted array>> sorted = [].</li>
<li>The first element of the input array (input[0] = 8).<ul><li>The sorted array is empty, we append the value to the sorted array: sorted =[8]</li></ul></li>
<li>The next input array (input[1] = 4).<ul>
<li>Compare 4 with each element in the sorted array (8)</li>
<li>4 is less than 8,  insert it before 8</li><li>Shift 8 one position to the right</li><li>Insert 4 at the first position in the sorted array: sorted = [4, 8].</li></ul></li>
<li> the next element of the input array (input[2] = 23).<ul><li>Compare 23 with each element in the sorted array (4, 8)</li><li>23 is greater than 8</li><li>Append 23 to the end of the sorted array: sorted = [4, 8, 23].</li></ul></li>
<li>The next element of the input array (input[3] = 42).<ul><li>Compare 42 with each element in the sorted array (4, 8, 23)</li><li>42 is greater than 23,leave it as is</li><li>Append 42 to the end of the sorted array: sorted = [4, 8, 23, 42].</li></ul></li>
<li>next element of the input array is (input[4] = 16).<ul><li>Compare 16 with each element in the sorted array (4, 8, 23, 42).</li><li>16 is less than 23,insert it before 23</li><li>Shift 23 and 42 one position to the right.</li><li>Insert 16 at the third position in the sorted array: sorted = [4, 8, 16, 23, 42].</li></ul></li>
<li>next element of the input array (input[5] = 15).<ul><li>Compare 15 with each element in the sorted array (4, 8, 16, 23, 42).
</li><li>15 is less than 16, insert it before 16.
</li><li>Shift 16, 23, 42 one position to the right.</li><li>Insert 15 at the third position in the sorted array: sorted = [4, 8, 15, 16, 23, 42].</li></ul></li>
</ol>

* Visual representation: [4, 8, 15, 16, 23, 42].

---

## Implementing Insertion Sort in Python

```python
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
```

```python
arr = [8, 4, 23, 42, 16, 15]
sorted_arr = InsertionSort(arr)
print(sorted_arr)
```
---

## conclusion

* Insertion Sort is an efficient sorting algorithm for small input sizes or partially sorted arrays.

* Not the most efficient algorithm for large arrays, it has a time complexity of **O(n^2)** in the worst case and **O(n)** in the best case for already sorted arrays.

* It has the advantage of being an in-place sorting algorithm, meaning it does not require additional memory beyond the input array.