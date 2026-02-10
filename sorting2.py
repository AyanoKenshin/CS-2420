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
    if len(A) <= 1:
        return

    mid = len(A) // 2
    L = A[:mid]
    R = A[mid:]

    MergeSort(L)
    MergeSort(R)

    for i in range(len(A)):
        if not R or (L and L[0] <= R[0]):
            A[i] = L.pop(0)
        else:
            A[i] = R.pop(0)

def QuickSort(A):
    QuickSortR(A, 0, len(A) - 1)

def QuickSortR(A, low, high):
    if low >= high:
        return

    boundary = low + 1

    for i in range(low + 1, high + 1):
        if A[i] < A[low]:
            A[i], A[boundary] = A[boundary], A[i]
            boundary += 1

    pivot = boundary - 1
    A[low], A[pivot] = A[pivot], A[low]

    QuickSortR(A, low, pivot - 1)
    QuickSortR(A, pivot + 1, high)

def ModifiedQuickSort(A):
    ModifiedQuickSortR(A, 0, len(A) - 1)

def ModifiedQuickSortR(A, low, high):
    if low >= high:
        return

    mid = (low + high) // 2
    A[low], A[mid] = A[mid], A[low]

    boundary = low + 1

    for i in range(low + 1, high + 1):
        if A[i] < A[low]:
            A[i], A[boundary] = A[boundary], A[i]
            boundary += 1

    pivot = boundary - 1
    A[low], A[pivot] = A[pivot], A[low]

    ModifiedQuickSortR(A, low, pivot - 1)
    ModifiedQuickSortR(A, pivot + 1, high)

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