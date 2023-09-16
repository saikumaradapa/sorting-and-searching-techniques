import time
start = time.time()


# array = [33, 22, 88, 66, 11, 44, 55, 77, 99]
array = [x for x in range(100000)]

'''
Bubble Sort: Bubble Sort compares adjacent elements and swaps them if they are in the wrong order. 
It repeatedly passes through the array until the entire array is sorted.
Best Case: O(n) - when the array is already sorted.
Worst Case: O(n^2) - when the array is in reverse order.'''
def bubble_sort(arr) :
    n = len(arr)
    for i in range(n) :
        for j in range(n-i-1) :
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)



'''
optimized Bubble Sort : In the best case scenario, where the input array is already sorted, 
the algorithm only requires a single pass through the array to confirm that it is sorted. 
Hence, the time complexity is linear, which is O(n).
Best Case: O(n)
Worst Case: O(n^2)'''
def optimized_bubble_sort(arr) :
    already_sorted = True
    n = len(arr)
    for i in range(n) :
        for j in range(n-i-1) :
            if arr[j] > arr[j+1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                already_sorted = False
        if already_sorted :
            break
    print(arr)



'''
Insertion Sort: Description: Insertion Sort builds the final sorted array one element at a time. 
It iterates through the array, comparing each element with its adjacent elements and 
inserting it at the correct position in the sorted region.
Best Case: O(n) - when the array is already sorted.
Worst Case: O(n^2) - when the array is in reverse order.'''
def insertion_sort(arr) :
    i = 1
    n = len(arr)
    while i < n :
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j - 1], arr[j]
            j -= 1
        i += 1
    print("insertion sort : ",arr)



'''
Selection Sort: Selection Sort divides the array into a sorted and an unsorted region. 
It repeatedly selects the smallest element from the unsorted region and 
swaps it with the first element of the unsorted region.
Best Case: O(n^2) - same as the worst case.
Worst Case: O(n^2) - when the array is in reverse order.'''
def selection_sort(arr) :
    n = len(arr)
    for i in range(n) :
        currMin = i
        for j in range(i+1, n) :
            if arr[currMin] > arr[j] :
                currMin = j
        arr[i], arr[currMin] = arr[currMin], arr[i]
    print(arr)



'''
Merge Sort: Merge Sort follows the divide-and-conquer approach. 
It recursively divides the array into smaller subarrays, sorts them, and 
then merges them back together.
Best Case: O(n log n) - when the array is already sorted or nearly sorted.
Worst Case: O(n log n) - for all input arrays.'''
def mergesort(arr) :
    if len(arr) > 1 :
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]
        mergesort(left)
        mergesort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right) :
            if left[i] < right[j] :
                arr[k] = left[i]
                i += 1
            else :
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left) :
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right) :
            arr[k] = right[j]
            j += 1
            k += 1
        print(arr)



'''
Quick Sort: Quick Sort also follows the divide-and-conquer approach. 
It selects a pivot element, partitions the array into two subarrays based on the pivot, and 
recursively sorts the subarrays.
Best Case: O(n log n) - when the pivot divides the array into two roughly equal-sized subarrays.
Worst Case: O(n^2) - when the pivot consistently partitions the array into subarrays of size 0 and n-1.'''
def quick_sort(arr, left, right) :
    if left < right :
        partition_position = partition(arr, left, right)
        quick_sort(arr, left, partition_position-1)
        quick_sort(arr, partition_position+1, right)
    # print(arr)
    return arr
def partition(arr, left, right) :
    i = left
    j = right -1
    pivote = arr[right]
    while i < j :
        while i < right and arr[i] < pivote :
            i += 1
        while j > left and arr[j] >= pivote :
            j -= 1
        if i < j :
            arr[i], arr[j] = arr[j], arr[i]
        if arr[i] > pivote :
            arr[i], arr[right] = arr[right], arr[i]

    return i


'''Linear Search:
Best Case Time Complexity: O(1)
Worst Case Time Complexity: O(n)'''
def linear_search(arr, target) :
    for i in range(len(arr)) :
        if arr[i] == target :
            print("target",target ,"found at index : ", i)
            return i
    print("target", target, "not found")

'''Binary Search:
Best Case Time Complexity: O(1)
Worst Case Time Complexity: O(log n)'''
def binary_search(arr, target) :
    arr.sort()
    left, right = 0, len(arr)-1
    while left < right :
        mid = (left+right+1) // 2
        if target == arr[mid] :
            print("target",target ,"found at index : ", mid)
            return
        elif target < arr[mid] :
            right = mid-1
        else :
            left = mid+1
    print("target",target ,"not found")






# bubble_sort(array)
# optimized_bubble_sort(array)
# insertion_sort(array)
# selection_sort(array)
# mergesort(array)
# quick_sort(array, 0, len(array)-1)

# linear_search(array, 5000000)
binary_search(array, 50000000)
# print(array)

end = time.time()
print("time to evaluate output : ",end - start)
