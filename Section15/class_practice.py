# Testing how to use classes.

import datetime

class Employee:

    num_emps = 0
    raise_amnt = 1.04

    def __init__(self, first, last, pay):
            self.first = first
            self.last = last
            self.pay = pay

            Employee.num_emps += 1

    def fullname(self):
        return '%s %s' % (self.first, self.last)

    def details(self):
        return '%s\n%s\n%d\n' % (self.first, self.last, self.pay)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amnt)

    @classmethod
    def set_raise_amnt(cls, amount):
        cls.raise_amnt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))


    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Jesse', 'Delia', 60000)

emp_1.apply_raise()
print(emp_1.details())
Employee.set_raise_amnt(1.05)

print(Employee.raise_amnt)
print(emp_1.details())

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.details())


my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))
