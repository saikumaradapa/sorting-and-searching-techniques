import time

# Start the timer to measure the execution time
start = time.time()

# Sample array with numbers from 0 to 99999
array = [x for x in range(100000)]

'''
Bubble Sort:
- Compares adjacent elements and swaps them if they are in the wrong order.
- Repeatedly passes through the array until the entire array is sorted.
Time Complexity:
- Best Case: O(n) for an already sorted array.
- Worst Case: O(n^2) for an array in reverse order.
'''
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)

'''
Optimized Bubble Sort:
- If during a pass no elements are swapped, it means the array is sorted.
Time Complexity:
- Best Case: O(n) for an already sorted array.
- Worst Case: O(n^2) for an array in reverse order.
'''
def optimized_bubble_sort(arr):
    already_sorted = True
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                already_sorted = False
        if already_sorted:
            break
    print(arr)

'''
Insertion Sort:
- Builds the final sorted array one element at a time.
- Iterates through the array, comparing each element with its adjacent elements, and inserting it at the correct position.
Time Complexity:
- Best Case: O(n) for an already sorted array.
- Worst Case: O(n^2) for an array in reverse order.
'''
def insertion_sort(arr):
    i = 1
    n = len(arr)
    while i < n:
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
        i += 1
    print("insertion sort:", arr)

'''
Selection Sort:
- Divides the array into a sorted and an unsorted region.
- Repeatedly selects the smallest element from the unsorted region and swaps it with the first element of the unsorted region.
Time Complexity:
- Best and Worst Case: O(n^2)
'''
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        currMin = i
        for j in range(i+1, n):
            if arr[currMin] > arr[j]:
                currMin = j
        arr[i], arr[currMin] = arr[currMin], arr[i]
    print(arr)

'''
Merge Sort:
- Divide-and-conquer approach.
- Recursively divides the array into smaller subarrays, sorts them, and merges them back together.
Time Complexity:
- Best and Worst Case: O(n log n)
'''
def mergesort(arr):
    if len(arr) > 1:
        # Split the list in half
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]

        # Recursively sort both halves
        mergesort(left)
        mergesort(right)

        # Merge the sorted lists into a new one
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # If left list still has values, add them to merged list
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # If right list still has values, add them to merged list
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        print(arr)

'''
Quick Sort:
- Divide-and-conquer approach.
- Selects a pivot element, partitions the array into two subarrays based on the pivot, and recursively sorts the subarrays.
Time Complexity:
- Best Case: O(n log n) when the pivot divides the array evenly.
- Worst Case: O(n^2) when the pivot does not divide the array evenly.
'''
def quick_sort(arr, left, right):
    if left < right:
        partition_position = partition(arr, left, right)
        quick_sort(arr, left, partition_position-1)
        quick_sort(arr, partition_position+1, right)
    return arr

def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i

'''
Linear Search:
- Iterates through the array looking for the target.
Time Complexity:
- Best Case: O(1) if the target is the first element.
- Worst Case: O(n) if the target is the last element or not present.
'''
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            print("target", target, "found at index:", i)
            return i
    print("target", target, "not found")

'''
Binary Search:
- Repeatedly divides the sorted array into halves until the target is found or the interval is empty.
Time Complexity:
- Best Case: O(1) if the target is the middle element.
- Worst Case: O(log n)
'''
def binary_search(arr, target):
    arr.sort()
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            print("target", target, "found at index:", mid)
            return
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    print("target", target, "not found")


# Uncomment the sorting or searching functions below to test them
# bubble_sort(array)
# optimized_bubble_sort(array)
# insertion_sort(array)
# selection_sort(array)
# mergesort(array)
# quick_sort(array, 0, len(array)-1)
# linear_search(array, 5000000)
binary_search(array, 50000000)

end = time.time()
print("time to evaluate output:", end - start)


