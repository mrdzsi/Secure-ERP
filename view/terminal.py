def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    print(title +": ")
    for index, option in enumerate(list_options[1:], start=1):
        print(f"({index}) {option}")
        if index == len(list_options)-1:
            print(f"(0) {list_options[0]}")


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    if type(result) == int or float:
        print(f"{label}: {round(result, 2)}")
    elif type(result) == list or tuple:
        print(f"{label}:\n{'; '.join(result)}")
    elif type(result) == dict:
        result ="; ".join(f"{key}: {value}" for key,value in result.items())
        print(f"{label}:\n{result}")


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \--------------------------------/
def print_table(table):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    column_numbers = len(max(table))  #  the first list in our table of list of lists
    
    longest_elem = None
    for row in table:
        longest_elem = max(row)
    column_width = len(longest_elem)

    first_line = "/" + ("-"*(((column_width+1)*column_numbers)-1)) + "\\"
    print(first_line)

    for row in table:
        line = "|" + "|".join(item.center(column_width) for item in row) + "|"
        fill = "|" + "|".join(("-"*column_width) for _ in row) + "|"
        print(line)
        print(fill)

    last_line = "\\" + ("-"*(((column_width+1)*column_numbers)-1)) + "/"
    print(last_line)


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    user_input = input(label)
    return user_input


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    user_input_list = []
    for element in labels:
        user_input_list.append(input(f"{element}"))
    return user_input_list


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(message)
