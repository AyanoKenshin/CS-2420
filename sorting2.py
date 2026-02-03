import random

def CreateRandomList(Size):
    rand_list = []
    for i in range(Size):
        rand_list.append(random.randint(0, Size - 1))
    return rand_list

def BubbleSort(A):
    sorted = False
    n = len(A)

    while not sorted:
        sorted = True
        for i in range(n - 1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                sorted = False

def ShakerSort(A):
    left = 0
    right = len(A) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(left, right):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                sorted = False
        right -= 1

        for i in range(right, left, -1):
            if A[i - 1] > A[i]:
                A[i - 1], A[i] = A[i], A[i - 1]
                sorted = False
        left += 1

def CountingSort(A):
    n = len(A)
    counts = [0] * n

    for x in A:
        counts[x] += 1

    i = 0
    for value in range(n):
        for _ in range(counts[value]):
            A[i] = value
            i += 1

def MergeSort(A):
    temp = [0] * len(A)
    _MergeSort(A, 0, len(A) - 1, temp)

def _MergeSort(A, low, high, temp):
    if low >= high:
        return

    mid = (low + high) // 2
    _MergeSort(A, low, mid, temp)
    _MergeSort(A, mid + 1, high, temp)
    _Merge(A, low, mid, high, temp)

def _Merge(A, low, mid, high, temp):
    i = low
    j = mid + 1
    k = low

    while i <= mid and j <= high:
        if A[i] <= A[j]:
            temp[k] = A[i]
            i += 1
        else:
            temp[k] = A[j]
            j += 1
        k += 1

    while i <= mid:
        temp[k] = A[i]
        i += 1
        k += 1

    while j <= high:
        temp[k] = A[j]
        j += 1
        k += 1

    for x in range(low, high + 1):
        A[x] = temp[x]

def QuickSort(A):
    _QuickSort(A, 0, len(A) - 1)

def _QuickSort(A, low, high):
    if low >= high:
        return

    p = _Partition(A, low, high)
    _QuickSort(A, low, p - 1)
    _QuickSort(A, p + 1, high)

def _Partition(A, low, high):
    pivot = A[low]
    left = low + 1
    right = high

    while True:
        while left <= right and A[left] <= pivot:
            left += 1
        while left <= right and A[right] >= pivot:
            right -= 1
        if left > right:
            break
        A[left], A[right] = A[right], A[left]

    A[low], A[right] = A[right], A[low]
    return right

def ModifiedQuickSort(A):
    _ModifiedQuickSort(A, 0, len(A) - 1)

def _ModifiedQuickSort(A, low, high):
    if low >= high:
        return

    mid = (low + high) // 2
    A[low], A[mid] = A[mid], A[low]

    p = _Partition(A, low, high)
    _ModifiedQuickSort(A, low, p - 1)
    _ModifiedQuickSort(A, p + 1, high)

def main():
    A = CreateRandomList(10)
    B = []

    for i in range(len(A)):
        B.append(A[i])

    BubbleSort(A)
    B.sort()

    if A == B:
        print("BubbleSort works")
    else:
        print("BubbleSort fails")

    A = CreateRandomList(10)
    B = []

    for i in range(len(A)):
        B.append(A[i])

    ShakerSort(A)
    B.sort()

    if A == B:
        print("ShakerSort works")
    else:
        print("ShakerSort fails")

    A = CreateRandomList(10)
    B = []

    for i in range(len(A)):
        B.append(A[i])

    CountingSort(A)
    B.sort()

    if A == B:
        print("CountingSort works")
    else:
        print("CountingSort fails")

    A = CreateRandomList(10)
    B = []

    for i in range(len(A)):
        B.append(A[i])

    MergeSort(A)
    B.sort()

    if A == B:
        print("MergeSort works")
    else:
        print("MergeSort fails")

    A = CreateRandomList(10)
    B = []

    for i in range(len(A)):
        B.append(A[i])

    QuickSort(A)
    B.sort()

    if A == B:
        print("QuickSort works")
    else:
        print("QuickSort fails")

    A = CreateRandomList(10)
    B = []

    for i in range(len(A)):
        B.append(A[i])

    ModifiedQuickSort(A)
    B.sort()

    if A == B:
        print("ModifiedQuickSort works")
    else:
        print("ModifiedQuickSort fails")

if __name__ == "__main__":
    main()