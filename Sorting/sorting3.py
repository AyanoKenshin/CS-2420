import random
import math

def MakeRandomData(size):
    A = []
    for _ in range(size):
        A.append(random.randrange(size))
    return A

def MakeMostlySortedData(size):
    A = MakeRandomData(size)
    A.sort()
    if size > 1:
        temp = A[0]
        A[0] = A[size - 1]
        A[size - 1] = temp
    return A

def CopyList(A):
    B = []
    for i in range(len(A)):
        B.append(A[i])
    return B

def BubbleSort(A):
    work = 0
    sorted = False
    n = len(A)

    while not sorted:
        sorted = True
        for i in range(n - 1):
            work += 1  # compare
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                work += 3  # swap = 3 copies
                sorted = False
    return work


def ShakerSort(A):
    work = 0
    left = 0
    right = len(A) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(left, right):
            work += 1  # compare
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                work += 3
                sorted = False
        right -= 1

        for i in range(right, left, -1):
            work += 1  # compare
            if A[i - 1] > A[i]:
                A[i - 1], A[i] = A[i], A[i - 1]
                work += 3
                sorted = False
        left += 1

    return work


def CountingSort(A):
    n = len(A)
    counts = [0] * n

    for x in A:
        counts[x] += 1

    work = 0
    i = 0
    for value in range(n):
        for _ in range(counts[value]):
            A[i] = value
            work += 1  # copy into A
            i += 1

    return work


def MergeSort(A):
    work = [0]
    MergeSortR(A, work)
    return work[0]

def MergeSortR(A, work):
    if len(A) <= 1:
        return

    mid = len(A) // 2
    L = A[:mid]
    R = A[mid:]

    MergeSortR(L, work)
    MergeSortR(R, work)

    for i in range(len(A)):
        if not R:
            A[i] = L.pop(0)
            work[0] += 1              # copy into A
            work[0] += (len(L))       # pop(0) shifts remaining items
        elif not L:
            A[i] = R.pop(0)
            work[0] += 1
            work[0] += (len(R))
        else:
            work[0] += 1              # compare L[0] <= R[0]
            if L[0] <= R[0]:
                A[i] = L.pop(0)
                work[0] += 1
                work[0] += (len(L))
            else:
                A[i] = R.pop(0)
                work[0] += 1
                work[0] += (len(R))


def QuickSort(A):
    return QuickSortR(A, 0, len(A) - 1)

def QuickSortR(A, low, high):
    if low >= high:
        return 0

    work = 0
    boundary = low + 1

    for i in range(low + 1, high + 1):
        work += 1  # compare A[i] < A[low]
        if A[i] < A[low]:
            A[i], A[boundary] = A[boundary], A[i]
            work += 3  # swap copies
            boundary += 1

    pivot = boundary - 1
    A[low], A[pivot] = A[pivot], A[low]
    work += 3

    work += QuickSortR(A, low, pivot - 1)
    work += QuickSortR(A, pivot + 1, high)

    return work


def ModifiedQuickSort(A):
    return ModifiedQuickSortR(A, 0, len(A) - 1)

def ModifiedQuickSortR(A, low, high):
    if low >= high:
        return 0

    work = 0

    mid = (low + high) // 2
    A[low], A[mid] = A[mid], A[low]
    work += 3

    boundary = low + 1

    for i in range(low + 1, high + 1):
        work += 1
        if A[i] < A[low]:
            A[i], A[boundary] = A[boundary], A[i]
            work += 3
            boundary += 1

    pivot = boundary - 1
    A[low], A[pivot] = A[pivot], A[low]
    work += 3

    work += ModifiedQuickSortR(A, low, pivot - 1)
    work += ModifiedQuickSortR(A, pivot + 1, high)

    return work

def RunOneTable(title, data):
    print(title)
    print("    Bubble   Shaker  Counting   Merge    Quick   MQuick")

    n = 8
    while n <= 2048:
        base = data(n)

        A = CopyList(base)
        b = BubbleSort(A)

        A = CopyList(base)
        s = ShakerSort(A)

        A = CopyList(base)
        c = CountingSort(A)

        A = CopyList(base)
        m = MergeSort(A)

        A = CopyList(base)
        q = QuickSort(A)

        A = CopyList(base)
        mq = ModifiedQuickSort(A)

        logn = int(math.log2(n))
        print(f"{logn:02d}  {math.log2(b):7.2f}  {math.log2(s):7.2f}  {math.log2(c):8.2f}  {math.log2(m):7.2f}  {math.log2(q):7.2f}  {math.log2(mq):7.2f}")

        n *= 2

    print()

def main():
    RunOneTable("Counting work when sorting random data:", MakeRandomData)
    RunOneTable("Counting work when sorting mostly sorted data:", MakeMostlySortedData)

if __name__ == "__main__":
    main()