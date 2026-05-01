from BagHash import Bag
from Students import Student
from time import perf_counter

def main():

    bag = Bag()

    insertT = perf_counter()
    f = open("FakeNames.txt", "r")
    for line in f:
        parts = line.strip().split()
        student = Student(parts[1], parts[0], parts[2], parts[3], parts[4])
        i_val = bag.Insert(student)
        if not i_val:
            print(f"Failed to Insert: {parts[1]} {parts[0]}")
    f.close()
    insertTdone = perf_counter() - insertT
    print(f"Time Spent Inserting: {insertTdone} ")

    inBag = bag.Size()
    print(f"Number of Students in Bag: {inBag}")

    ageT = perf_counter()
    total_age = 0
    for item in bag:
        total_age += item.age
    avg_age = total_age / inBag
    print(f"Average Age of All Students: {format(avg_age, '.4f')}")
    ageTdone = perf_counter() - ageT
    print(f"Time Spent Averaging Ages: {ageTdone}")

    deleteT = perf_counter()
    f = open("DeleteNames.txt", "r")
    for line in f:
        ssn = line.strip()
        temp = Student("", "", ssn, "", 0)
        d_val = bag.Delete(temp)
        if not d_val:
            print(f"Failed To Delete: {ssn}")
    f.close()
    deleteTdone = perf_counter() - deleteT
    print(f"Time Spent Deleting: {deleteTdone}")

    nowInBag = bag.Size()
    print(f"Students in Bag After Deletion: {nowInBag}")

    retrieveT = perf_counter()
    r_total_age = 0
    r_count = 0
    f = open("RetrieveNames.txt", "r")
    for line in f:
        ssn = line.strip()
        temp = Student("", "", ssn, "", 0)
        r_val = bag.Retrieve(temp)
        if r_val:
            r_total_age += r_val.age
            r_count += 1
        else:
            print(f"Failed To Retrieve: {ssn}")
    r_avgAge = r_total_age / r_count if r_count > 0 else 0.0
    print(f"Average Age of Retrieved Students: {format(r_avgAge, '.4f')}")
    f.close()
    retrieveTdone = perf_counter() - retrieveT
    print(f"Time Spent Retrieving: {retrieveTdone}")

if __name__ == "__main__":
    main()