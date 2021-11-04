from hr import get_oldest_youngest
from model.hr import hr
from view import terminal as view


def list_employees():
    table = hr.get_table()
    print(table)


def add_employee():
    id = view.get_input("id")
    name = view.get_input("name")
    bday = view.get_input("birthday")
    department = view.get_input("department")
    security_lvl = view.get_input("security clearance level")


def update_employee():
    employee_id = view.get_input("which employee to update?: ")
    ask = view.get_input("What info needs to be updated? (1,2,3,4,5): ")
    new_info = view.get_input("Type in new info: ")


def delete_employee():
    employee_id = view.get_input("which employee to delete?: ")
    hr.delete_employee(employee_id)


def get_oldest_and_youngest():
    oldest, youngest, oldest_name, youngest_name = hr.get_oldest_youngest()
    view.print_message(f"The youngest is {youngest_name} who was born in {youngest}")
    view.print_message(f"The oldest is {oldest_name} who was born in {oldest}")


def get_average_age():
    view.print_error_message("Not implemented yet.")


def next_birthdays():
    current_date = view.get_input("Type in current date in YYYY-MM-DD format: ")
    upcoming_bdays = next_birthday_calc(current_date)
    view.print_message(f"upcoming bdays are: {upcoming_bdays}")


def count_employees_with_clearance():
    clearance_lvl = view.get_input("Minimum level security clearance: ")
    have_clearance = hr.have_clearance(clearance_lvl)
    view.print_message(f"These employees have minimum clearance level: {have_clearance}")


def count_employees_per_department():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)