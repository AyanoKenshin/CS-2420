class Student:

    def __init__(self, first, last, ssn, email, age):
        self.first = first
        self.last = last
        self.ssn = ssn
        self.email = email
        self.age = int(age)

    def __eq__(self, rhs):
        return self.ssn == rhs.ssn

    def __lt__(self, rhs):
        return self.ssn < rhs.ssn

    def __str__(self):
        return self.first + " " + self.last + " " + self.ssn + " " + self.email + " " + str(self.age)