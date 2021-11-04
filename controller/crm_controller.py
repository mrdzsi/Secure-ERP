from model.crm import crm
from view import terminal as view


def list_customers():
    names = crm.list_of_customers()
    view.print_table(names)


def add_customer():
    name = view.get_input("Please enter your name")
    email = view.get_input("Please enter your email adress")
    subscription = view.get_input("Are you subscibed? 1 : yes, 0 :  no")
    crm.new_customer(name, email, subscription)


def update_customer():
    id = view.get_input("Please enter your id")
    name = view.get_input("Please enter your new name")
    email = view.get_input("Please enter your new email adress")
    subscription = view.get_input("Are you subscibed? 1 : yes, 0 :  no")
    is_updated = crm.change_customer_data(id, name, email, subscription)
    if is_updated is False:
        view.print_error_message("ID not found")


def delete_customer():
    id = view.get_input("Please enter the id for deletion")
    is_deleted = crm.change_customer_data(id)
    if is_deleted is True:
        view.print_error_message("ID not found")


def get_subscribed_emails():
    crm.subscribed_customers()


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
