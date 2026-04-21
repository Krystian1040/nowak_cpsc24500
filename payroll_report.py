#Assignment #4- Payroll System
#payroll_report.py
#Christian Nowak
#OOP


class PayrollReport:
    def __init__(self, processor):
        self.processor = processor

    def display_all_employees(self):
        print("\nEmployee List")
        print("-" * 50)

        for emp in self.processor.employees:
            print(f"{emp.name} | {emp.employee_id} | ${emp.hourly_rate:.2f} | "
                  f"{emp.hours_worked} hrs | ${emp.calculate_gross_pay():.2f}")

    def display_payroll_summary(self):
        print("\nPayroll Summary")
        print("-" * 50)

        print("Total Employees:", self.processor.get_employee_count())
        print("Total Payroll: $", round(self.processor.calculate_total_payroll(), 2))
        print("Average Pay: $", round(self.processor.calculate_average_pay(), 2))

        highest = self.processor.find_highest_paid()
        lowest = self.processor.find_lowest_paid()

        if highest:
            print("Highest Paid:", highest.name, f"(${highest.calculate_gross_pay():.2f})")

        if lowest:
            print("Lowest Paid:", lowest.name, f"(${lowest.calculate_gross_pay():.2f})")

    def generate_report_file(self, filename):
        with open(filename, "w") as file:
            file.write("Payroll Report\n")
            file.write("-" * 40 + "\n")

            for emp in self.processor.employees:
                file.write(str(emp) + "\n")