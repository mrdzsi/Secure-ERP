from model.sales import sales
from view import terminal as view


def list_transactions():
    table = sales.list_transactions()
    view.print_table(table)


def add_transaction():
    price_input = view.get_input("Please enter the price of the transaction")
    product_input = view.get_input("Please enter the product of the transaction")
    transaction_date = view.get_input("Please enter the date of the transaction")
    sales.add_transaction(price_input, product_input, transaction_date)


def update_transaction():
    transaction_input_id = view.get_input("Please enter the ID of the transaction")
    product = view.get_input("Please enter the new name of the product")
    price = view.get_input("Please enter the new price of the transaction")
    transaction_date = view.get_input("Please enter the new date of the transaction")
    sales.update_transaction(transaction_input_id, product, price, transaction_date)


def delete_transaction():
    wanted_transaction_input_id = view.get_input("Please enter the ID of the transaction")
    sales.delete_transaction(wanted_transaction_input_id)


def get_biggest_revenue_transaction():
    table = sales.get_biggest_revenue_transaction()
    view.print_table(table)


def get_biggest_revenue_product():
    biggest_revenue = sales.get_biggest_revenue_product()
    view.print_general_results(biggest_revenue, "Biggest revenue")


def count_transactions_between():
    date1 = view.get_input("Please enter the first date")
    date2 = view.get_input("Please enter the second date")
    count = sales.count_transactions_between(date1, date2)
    view.print_general_results(count, f"Transactions between {date1} and {date2}")


def sum_transactions_between():
    date1 = view.get_input("Please enter the first date")
    date2 = view.get_input("Please enter the second date")
    sum = sales.sum_transactions_between(date1, date2)
    view.print_general_results(sum, f"Sum of transactions between {date1} and {date2}")


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation: ")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)