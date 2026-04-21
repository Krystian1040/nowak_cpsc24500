#Assignment #4- Payroll System
#payroll_processor.py
#Christian Nowak
#OOP

from employee import Employee


class PayrollProcessor:
    def __init__(self):
        self._employees = []

    @property
    def employees(self):
        return self._employees.copy()

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                for line in file:
                    line = line.strip()

                    if line == "":
                        continue

                    parts = line.split("\t")

                    if len(parts) != 4:
                        print("Warning: invalid line skipped")
                        continue

                    try:
                        name = parts[0]
                        employee_id = parts[1]
                        hourly_rate = parts[2]
                        hours_worked = parts[3]

                        employee = Employee(name, employee_id, hourly_rate, hours_worked)
                        self._employees.append(employee)

                    except ValueError:
                        print("Warning: bad employee data skipped")

        except FileNotFoundError:
            print("Error: file not found")

    def calculate_total_payroll(self):
        total = 0
        for emp in self._employees:
            total += emp.calculate_gross_pay()
        return total

    def find_highest_paid(self):
        if not self._employees:
            return None
        highest = self._employees[0]
        for emp in self._employees:
            if emp.calculate_gross_pay() > highest.calculate_gross_pay():
                highest = emp
        return highest

    def find_lowest_paid(self):
        if not self._employees:
            return None
        lowest = self._employees[0]
        for emp in self._employees:
            if emp.calculate_gross_pay() < lowest.calculate_gross_pay():
                lowest = emp
        return lowest

    def get_employee_count(self):
        return len(self._employees)

    def calculate_average_pay(self):
        if len(self._employees) == 0:
            return 0
        return self.calculate_total_payroll() / len(self._employees)
    