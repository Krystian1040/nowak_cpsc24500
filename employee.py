#Assignment #4- Payroll System
#employee.py
#Christian Nowak
#OOP

#employee details
class Employee:
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        self.name = name
        self.employee_id = employee_id
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

     # name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        value = value.strip()
        if value == "":
            raise ValueError("Invalid name")
        self._name = value

    # employee id
    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        value = value.strip()
        if value == "":
            raise ValueError("Invalid ID")
        self._employee_id = value

    # hourly rate
    @property
    def hourly_rate(self):
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, value):
        if float(value) < 0:
            raise ValueError("Invalid rate")
        self._hourly_rate = float(value)

    # hours worked
    @property
    def hours_worked(self):
        return self._hours_worked

    @hours_worked.setter
    def hours_worked(self, value):
        if float(value) < 0 or float(value) > 168:
            raise ValueError("Invalid hours")
        self._hours_worked = float(value)

    #Calculation of pay
    def calculate_gross_pay(self):
        if self.hours_worked <= 40:
            return self.hourly_rate * self.hours_worked
        else:
            overtime_hours = self.hours_worked - 40
            regular_pay = 40 * self.hourly_rate
            overtime_pay = overtime_hours * (self.hourly_rate * 1.5)
            return regular_pay + overtime_pay
        
    def __str__(self):
        return f"{self.name} ({self.employee_id}) - ${self.calculate_gross_pay():.2f}"    