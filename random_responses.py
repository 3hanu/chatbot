import random

def random_string():
    random_list = [
        "I can't understand what you are saying",
        "Please try writing something more descriptive.",
        "I can't answer that yet, please try asking something else."
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]
