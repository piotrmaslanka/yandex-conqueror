import random

from .definitions import get_messages, get_messages_backend


def generate_message() -> str:
    random_msg = random.randint(1, 10)
    if random_msg < 7:
        return str(random.choice(get_messages('1-A')))
    else:
        return str(random.choice(get_messages('2-A'))+'\n'+ str(random.choice(get_messages('2-B'))))
    # else:
    #     return str(random.choice(get_messages('3-A'))) + '\n' + str(random.choice(get_messages('3-B')))\
    #          + '\n' + str(random.choice(get_messages('3-C'))) + '\n' + str(random.choice(get_messages('3-D'))) + '\n' \
    #          + str(random.choice(get_messages('3-E')))


def generate_message_client() -> str:
    random_msg = random.randint(1, 10)
    if random_msg < 7:
        return str(random.choice(get_messages_backend('1-A')))
    else:
        return str(random.choice(get_messages_backend('2-A'))+'\n'+ str(random.choice(get_messages_backend('2-B'))))
    # else:
    #     return str(random.choice(get_messages_backend('3-A'))) + '\n' + str(random.choice(get_messages_backend('3-B')))\
    #          + '\n' + str(random.choice(get_messages_backend('3-C'))) + '\n' + str(random.choice(get_messages_backend('3-D'))) + '\n' \
    #          + str(random.choice(get_messages_backend('3-E')))
