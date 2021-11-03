""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""


from model import data_manager, util


def new_customer():
    name = str(input('Enter the name'))
    email = str(input('Enter the email address'))
    subscribed = int(input('Is subscribed to the newsletter? 1: yes, 0: no'))
    while subscribed != 1 or 0:
        generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!")


def all_customers(file_name):
    with open(file_name, 'r') as file:
        data = file.readlines()
        print(data)


all_customers('crm.csv')


DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]
