""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""


from model import data_manager, util


def new_customer(name, email, subscription):
    id = util.generate_id()
    data = [id, name, email, subscription]
    customers = data_manager.read_table_from_file('crm.csv', ';')
    customers.append(data)
    data_manager.write_table_to_file('crm.csv', customers, ';')
    return data
  

DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]
