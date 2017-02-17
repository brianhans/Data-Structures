import math
from trees import BinaryTree

def bubble_sort(arr):
    swapped = True

    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

    return arr


def selection_sort(arr):
    for i in range(len(arr)):
        lowestIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[lowestIndex]:
                lowestIndex = j

        arr[i], arr[lowestIndex] = arr[lowestIndex], arr[i]

    return arr

def insertion_sort(arr):
    for i in range(len(arr)):
        for j in range(0, i):
            if arr[i] < arr[j]:
                arr.insert(j, arr[i])
                del arr[i + 1]

    return arr


def bucket_sort(arr, num = 5):
    if len(arr) <= 1:
        return arr

    buckets = []
    for i in range(num):
        buckets.append([])

    #Find the highest and lowest numbers in the array
    largest = arr[0]
    lowest = arr[0]
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
        elif arr[i] < lowest:
            lowest = arr[i]

    #Creates a range that is based off the variation in numbers and the amount of buckets
    bucket_range = int(math.ceil(float(largest - lowest) / num))

    for i in range(len(arr)):
        index = (arr[i] - lowest) / bucket_range
        buckets[index].append(arr[i])

    sorted_array = []
    for bucket in buckets:
        bubble_sort(bucket)
        sorted_array.extend(bucket)

    return sorted_array

def counting_sort(arr):
    if len(arr) <= 1:
        return arr

    histogram = []
    #Find the highest and lowest numbers in the array
    largest = arr[0]
    lowest = arr[0]
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
        elif arr[i] < lowest:
            lowest = arr[i]

    for i in range(largest - lowest + 1):
        histogram.append(0)

    for i in arr:
        histogram[i - 1] += 1

    sorted_array = []

    for i in range(len(histogram)):
        for _ in range(histogram[i]):
            sorted_array.append(i + lowest)

    return sorted_array

def merge_sort(arr):

    right_position = len(arr) / 2
    left_array = arr[:right_position]
    right_array = arr[right_position:]

    if (len(left_array) > 1 or len(right_array) > 1):
        left_array = merge_sort(left_array)
        right_array = merge_sort(right_array)

    return merge_arrays(left_array, right_array)

def merge_arrays(left_array, right_array):
    new_array = []
    left_pointer = 0
    right_pointer = 0

    left_length = len(left_array)
    right_length = len(right_array)

    while left_pointer < left_length and right_pointer < right_length:
        if left_array[left_pointer] < right_array[right_pointer]:
            new_array.append(left_array[left_pointer])
            left_pointer += 1
        else:
            new_array.append(right_array[right_pointer])
            right_pointer += 1

    if left_pointer >= left_length:
        new_array.extend(right_array[right_pointer:])
    elif right_pointer >= right_length:
        new_array.extend(left_array[left_pointer:])

    return new_array

def tree_sort(arr):
    bst = BinaryTree(arr)
    return bst.in_order_traverse()

def quick_sort(arr, start = 0, end = None):
    if end is None:
        end = len(arr) - 1

    if end - start < 1:
        return

    swap_index = start
    pivot = end


    for i in range(start, end):
        if arr[i] < arr[pivot]:
            arr[swap_index], arr[i] = arr[i], arr[swap_index]
            swap_index += 1

    arr[swap_index], arr[pivot] = arr[pivot], arr[swap_index]

    quick_sort(arr, start, swap_index - 1)
    quick_sort(arr, swap_index + 1, end)
