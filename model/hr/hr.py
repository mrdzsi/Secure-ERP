""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from os import remove
from model import data_manager, util

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]


def get_table():
    table = data_maganger.read_table_from_file("hr.csv")
    # with open("hr.csv", 'r') as file:
    #     data_dictionary = {}
    #     for line in file:
    #         data = line.split(";")  # itt az argument ("\n") vagy (";")?
    #         data_dictionary{"id": data[0], "name": data[1], "birth date": data[2], "department": data[3], "clearance level": data[4]}
    return table


# def del_employee(table):
#     del_this_user = input("Who do you want to delete from the system?: ")
#     for row in table:
#         if del_this_user == str(row[1]):
#             remove(row)
#     data_manager.write_table_to_file("hr.csv", table)


def delete_employee(employee_id):
    table = get_table()
    for row in table:
        if employee_id == str(row[0]):
            remove(row)
    data_manager.write_table_to_file("hr.csv", table)


def update_employee(employee_id, ask, new_info):
    table = get_table()
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
    data_manager.write_table_to_file("hr.csv", table)


def add_employee(id, name, bday, department, security_lvl):
    table = get_table()
    table.append[id, name, bday, department, security_lvl]
    data_manager.write_table_to_file("hr.csv", table)


def get_oldest_youngest():
    table = get_table()
    youngest = 0
    oldest = 10000
    for row in table:
        if int(row[2]) > youngest:
            youngest = row[2]
            youngest_name = row[1]
        if int(row[2]) < oldest:
            oldest = row[2]
            oldest_name = row[1]
    return oldest, youngest, oldest_name, youngest_name


def get_average_age():
    table = get_table()
    list_of_bdays = []
    for row in table:
        list_of_bdays.append(row[2])
    # gets a list of all birthdays, needs to calculate age from here
