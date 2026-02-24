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

if __name__ == "__main__":
    main()