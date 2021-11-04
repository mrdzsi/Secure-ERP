""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""
from model import data_manager, util


DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]
ID = 0
CUSTOMER_ID = 1
PRODUCT = 2
PRICE = 3
TRANSACTION_DATE = 4


def list_transactions():
    return data_manager.read_table_from_file(DATAFILE)


def add_transaction(price, product, transaction_date):
    table = data_manager.read_table_from_file(DATAFILE)
    new_transaction = [util.generate_id(), util.generate_id(), product, price, transaction_date]
    table.append(new_transaction)
    data_manager.write_table_to_file(DATAFILE, table) 


def update_transaction(transaction_id, product, price, transaction_date):
    table = data_manager.read_table_from_file(DATAFILE)
    for index, transaction in enumerate(table):
        if transaction_id in transaction:
            table[index] = [transaction_id, util.generate_id(), product, price, transaction_date]
    data_manager.write_table_to_file(DATAFILE, table)


def delete_transaction(transaction_id):
    table = data_manager.read_table_from_file(DATAFILE)
    for index, transaction in enumerate(table):
        if transaction_id in transaction:
            table.pop(index)
    data_manager.write_table_to_file(DATAFILE, table)


def get_biggest_revenue_transaction():
    table = data_manager.read_table_from_file(DATAFILE)
    biggest_revenue = table[0]
    for transaction in table:
        if float(transaction[PRICE]) > float(biggest_revenue[PRICE]):
            biggest_revenue = transaction
    return [biggest_revenue]


def get_biggest_revenue_product():
    table = data_manager.read_table_from_file(DATAFILE)
    revenues = []
    for transaction in table:
        for index in range(len(revenues)):
            if transaction[PRODUCT] in revenues[index]:
                revenues[index][PRICE] = str(float(revenues[index][PRICE]) + float(transaction[PRICE]))
                break
        else:
            revenues.append(transaction)
    biggest_revenue = revenues[0]

    for transaction in revenues:
        if float(transaction[PRICE]) > float(biggest_revenue[PRICE]):
            biggest_revenue = transaction
    return {"Product": biggest_revenue[PRODUCT], "Total revenue": biggest_revenue[PRICE]}


def count_transactions_between(date1, date2):
    table = data_manager.read_table_from_file(DATAFILE)
    start_date = util.parse_datetime(date1)
    end_date = util.parse_datetime(date2)
    counter = 0
    for transaction in table:
        transaction_date = util.parse_datetime(transaction[TRANSACTION_DATE])
        if transaction_date > start_date and transaction_date < end_date:
            counter += 1
    return counter


def sum_transactions_between(date1, date2):
    table = data_manager.read_table_from_file(DATAFILE)
    start_date = util.parse_datetime(date1)
    end_date = util.parse_datetime(date2)
    sum = 0
    for transaction in table:
        transaction_date = util.parse_datetime(transaction[TRANSACTION_DATE])
        if transaction_date > start_date and transaction_date < end_date:
            sum += float(transaction[PRICE])
    return sum