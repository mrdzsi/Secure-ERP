""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""


from model import data_manager, util


DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]


def new_customer(name, email, subscription):
    id = util.generate_id()
    data = [id, name, email, subscription]
    customers = data_manager.read_table_from_file(DATAFILE, ';')
    customers.append(data)
    data_manager.write_table_to_file(DATAFILE, customers, ';')


def list_of_customers():
    customers = data_manager.read_table_from_file(DATAFILE, ';')
    return customers


def change_customer_data(id, name, email, subscription):
    is_update_sucessfull = False
    costumers = data_manager.read_table_from_file(DATAFILE, ';')
    for costumer_index in range(len(costumers)):
        if id == costumers[costumer_index][0]:
            costumers[costumer_index][1] = name
            costumers[costumer_index][2] = email
            costumers[costumer_index][3] = subscription
            is_update_sucessfull = True
    data_manager.write_table_to_file(DATAFILE, costumers, ';')
    return is_update_sucessfull


def remove_customer_data(id):
    is_costumer = False
    costumers = data_manager.read_table_from_file(DATAFILE, ';')
    for costumer_index in range(len(costumers)):
        if id == costumers[costumer_index][0]:
            costumers.remove(costumers[costumer_index])
            is_costumer = True
    data_manager.write_table_to_file(DATAFILE, costumers, ';')
    return is_costumer


def subscribed_customers():
    subscribed_costumer = []
    costumers = data_manager.read_table_from_file(DATAFILE, ';')
    for costumer_index in range(len(costumers)):
        if 1 == costumers[costumer_index][3]:
            subscribed_costumer.append(costumers[costumer_index][2])
    return subscribed_costumer
