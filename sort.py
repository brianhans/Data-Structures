import math

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
    histogram = []
    #Find the highest and lowest numbers in the array
    largest = arr[0]
    lowest = arr[0]
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
        elif arr[i] < lowest:
            lowest = arr[i]

    for i in range(largest - lowest):
        histogram.append(0)

    for i in arr:
        histogram[i] += 1

    sorted_array = []

    for i in range(histogram):
        for _ in range(histogram[i]):
            sorted_array.append(i + lowest)

    return sorted_array
