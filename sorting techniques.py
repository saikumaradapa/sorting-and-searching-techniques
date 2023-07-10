import time
start = time.time()



array = [33, 22, 88, 66, 11, 44, 55, 77, 99]
array = [x for x in range(10000+1)]
def bubble_sort(arr) :
    n = len(arr)
    for i in range(n) :
        for j in range(n-i-1) :
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)




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

# bubble_sort(array)
# optimized_bubble_sort(array)
# insertion_sort(array)
# mergesort(array)

end = time.time()
print(end - start)
