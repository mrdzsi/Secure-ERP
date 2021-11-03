import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    generated_id = [random.choice(string.ascii_lowercase) for char in range(number_of_small_letters)]
    generated_id += [random.choice(string.ascii_uppercase) for char in range(number_of_capital_letters)]
    generated_id += [random.choice(string.digits) for char in range(number_of_digits)]
    generated_id += [random.choice(allowed_special_chars) for char in range(number_of_special_chars)]
    random.shuffle(generated_id)
    return "".join(generated_id)
