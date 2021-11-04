""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""


import datetime
from os import remove
from model import data_manager, util


DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]


def list_employees(file=DATAFILE):
    employees = data_manager.read_table_from_file(file)
    return employees


def new_employee(name, bday, department, security_lvl, file=DATAFILE):
    id = util.generate_id()
    data = [id, name, bday, department, security_lvl]
    employees = data_manager.read_table_from_file(file, ';')
    employees.append(data)
    data_manager.write_table_to_file(file, employees, ';')


def update_employee(employee_id, ask, new_info, file=DATAFILE):
    table = data_manager.read_table_from_file(file)
    for row in table:
        if employee_id == str(row[0]):
            # ask = input("What info needs to be updated? (1,2,3,4,5)")  # id, name, bday, department, security
            if ask == "1":
                row[0] = new_info
            if ask == "2":
                row[1] = new_info
            if ask == "3":
                row[2] = new_info
            if ask == "4":
                row[3] = new_info
            if ask == "5":
                row[4] = int(new_info)
    data_manager.write_table_to_file(file, table)


def delete_employee(employee_id, file=DATAFILE):
    table = data_manager.read_table_from_file(file)
    for row in table:
        if employee_id == str(row[0]):
            remove(row)
    data_manager.write_table_to_file(file, table)


# def add_employee(id, name, bday, department, security_lvl):
#     table = get_table()
#     table.append[id, name, bday, department, security_lvl]
#     data_manager.write_table_to_file(DATAFILE, table)


def get_oldest_youngest(file=DATAFILE):
    table = data_manager.read_table_from_file(file)
    youngest = 0
    youngest_month = 0
    youngest_day = 0
    oldest = 10000
    oldest_month = 12
    oldest_day = 31

    for row in table:
        birth_date = [str(row[2]).split("-")]
        year_of_birth = birth_date[0]
        month_of_birth = birth_date[1]
        day_of_birth = birth_date[2]

        if int(year_of_birth) > youngest:
            youngest = row[2]
            youngest_name = row[1]
        if int(year_of_birth) == youngest:
            if int(month_of_birth) > youngest_month:
                youngest = row[2]
                youngest_name = row[1]
        if int(year_of_birth) == youngest:
            if int(month_of_birth) == youngest_month:
                if int(day_of_birth) > youngest_day:
                    youngest = row[2]
                    youngest_name = row[1]

        if int(year_of_birth) < oldest:
            oldest = row[2]
            oldest_name = row[1]
        if int(year_of_birth) == oldest:
            if int(month_of_birth) < oldest_month:
                oldest = row[2]
                oldest_name = row[1]
        if int(year_of_birth) == oldest:
            if int(month_of_birth) == oldest_month:
                if int(day_of_birth) < oldest_day:
                    oldest = row[2]
                    oldest_name = row[1]
    return oldest, youngest, oldest_name, youngest_name


def get_average_age(file=DATAFILE):
    table = data_manager.read_table_from_file(file)
    today = datetime.date.today
    list_of_ages = []
    for row in table:
        birth_date = [str(row[2]).split("-")]
        year_of_birth = birth_date[0]
        month_of_birth = birth_date[1]
        day_of_birth = birth_date[2]
        birthday = datetime.date(int(year_of_birth), int(month_of_birth), int(day_of_birth))
        age = today - birthday  # ez lehet hogy napokban adja vissza a kort, nem tudom, tesztnél kiderül
        list_of_ages.append(age)

    nr_of_cycles = 0
    total = 0
    for element in list_of_ages:
        total += int(element)
        nr_of_cycles += 1
    average = total // nr_of_cycles  # ez lehet sima / is, nem tudom számít-e hogy kerekített átlag
    return average


def next_birthday_calc(current_date, file=DATAFILE):
    table = data_manager.read_table_from_file(file)
    today = datetime.date.today
    has_bday = []
    for row in table:
        birth_date = [str(row[2]).split("-")]
        year_of_birth = birth_date[0]
        month_of_birth = birth_date[1]
        day_of_birth = birth_date[2]
        birth = datetime.date(int(year_of_birth), int(month_of_birth), int(day_of_birth))
        if(
            today.month == birth.month
            and today.day >= birth.day
            or today.month > birth.month
        ):
            nextBirthdayYear = today.year + 1
        else:
            nextBirthdayYear = today.year

        nextBirthday = datetime.date(nextBirthdayYear, birth.month, birth.day)
        diff = nextBirthday - today
        if int(diff.days) <= 14:
            has_bday.append(row[1])
    return has_bday


def have_clearance(clearance_lvl, file=DATAFILE):
    table = data_manager.read_table_from_file(file)
    have_clearance = []
    for row in table:
        if int(row[4]) >= int(clearance_lvl):
            have_clearance.append(row[1])
    return have_clearance


def employees_per_department(file=DATAFILE):
    table = data_manager.read_table_from_file(file)
    departments = {}
    for row in table:
        if row[3] not in departments.keys():
            departments.update({f'{row[3]}': 1})
        else:
            departments[f"{row[3]}"] += 1
    return departments
