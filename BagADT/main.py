from Bag_PythonList import Bag
from Student import Student
from time import perf_counter


def main():

    b = Bag()

    start = perf_counter()

    f = open("FakeNames.txt", "r")
    for line in f:
        parts = line.strip().split()
        s = Student(parts[0], parts[1], parts[2], parts[3], parts[4])
        b.Insert(s)
    f.close()

    end = perf_counter()
    print("Insert time:", end - start)
    print("Size:", b.Size())

    total = 0
    count = 0

    for item in b:
        total += item.age
        count += 1

    print("Average age:", total / count)

    start = perf_counter()

    f = open("DeleteNames.txt", "r")
    for line in f:
        ssn = line.strip()
        temp = Student("", "", ssn, "", 0)
        b.Delete(temp)
    f.close()

    end = perf_counter()
    print("Delete time:", end - start)
    print("Size after delete:", b.Size())

    start = perf_counter()

    f = open("RetrieveNames.txt", "r")
    for line in f:
        ssn = line.strip()
        temp = Student("", "", ssn, "", 0)
        b.Retrieve(temp)
    f.close()

    end = perf_counter()
    print("Retrieve time:", end - start)


if __name__ == "__main__":
    main()