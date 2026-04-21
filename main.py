#Assignment #4- Payroll System
#main.py
#Christian Nowak
#OOP

from payroll_processor import PayrollProcessor
from payroll_report import PayrollReport


def main():
    processor = PayrollProcessor()
    processor.load_from_file("employees.txt")

    report = PayrollReport(processor)

    while True:
        print("\n" + "=" * 38)
        print("Payroll Management System")
        print("=" * 38)
        print("(1) View all employees")
        print("(2) View payroll summary")
        print("(3) Generate report file")
        print("(4) Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            report.display_all_employees()
        elif choice == "2":
            report.display_payroll_summary()
        elif choice == "3":
            report.generate_report_file("payroll_report.txt")
            print("Report file created successfully.")
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()