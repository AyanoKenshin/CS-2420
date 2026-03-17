from Bag_LinkedList import Bag
from Student import Student
from time import perf_counter


def main():

    b = Bag()

    failed_inserts = []

    start = perf_counter()

    f = open("FakeNames.txt", "r")
    for line in f:
        parts = line.strip().split()
        s = Student(parts[0], parts[1], parts[2], parts[3], parts[4])
        ok = b.Insert(s)
        if not ok:
            if len(failed_inserts) < 2:
                failed_inserts.append(s.first + " " + s.last)
    f.close()

    insert_time = perf_counter() - start

    for name in failed_inserts:
        print("Failed insert:", name)
    print("Insert time:", insert_time)
    print("Students in bag:", b.Size())

    start = perf_counter()

    total_age = 0
    count = 0
    for item in b:
        total_age += item.age
        count += 1

    avg_age_all = total_age / count if count > 0 else 0.0
    avg_time = perf_counter() - start

    print("Average age (all):", format(avg_age_all, ".4f"))
    print("Average age time:", avg_time)

    failed_deletes = []

    start = perf_counter()

    f = open("DeleteNames.txt", "r")
    for line in f:
        ssn = line.strip()
        temp = Student("", "", ssn, "", 0)
        ok = b.Delete(temp)
        if not ok:
            if len(failed_deletes) < 2:
                failed_deletes.append(ssn)
    f.close()

    delete_time = perf_counter() - start

    for ssn in failed_deletes:
        print("Failed delete:", ssn)
    print("Delete time:", delete_time)
    print("Students left in bag:", b.Size())

    failed_retrieves = []
    retrieved_total_age = 0
    retrieved_count = 0

    start = perf_counter()

    f = open("RetrieveNames.txt", "r")
    for line in f:
        ssn = line.strip()
        temp = Student("", "", ssn, "", 0)
        found = b.Retrieve(temp)
        if found is None:
            if len(failed_retrieves) < 2:
                failed_retrieves.append(ssn)
        else:
            retrieved_total_age += found.age
            retrieved_count += 1
    f.close()

    retrieve_time = perf_counter() - start

    avg_age_retrieved = retrieved_total_age / retrieved_count if retrieved_count > 0 else 0.0

    for ssn in failed_retrieves:
        print("Failed retrieve:", ssn)
    print("Average age (retrieved):", format(avg_age_retrieved, ".4f"))
    print("Retrieve time:", retrieve_time)


if __name__ == "__main__":
    main()