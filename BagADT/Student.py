class Student:

    def __init__(self, first, last, age, ssn):
        self.first = first
        self.last = last
        self.age = int(age)
        self.ssn = ssn

    def __eq__(self, rhs):
        return self.ssn == rhs.ssn

    def __str__(self):
        return self.first + " " + self.last + " " + str(self.age) + " " + self.ssn