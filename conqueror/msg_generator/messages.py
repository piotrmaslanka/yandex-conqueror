import random

from .definitions import get_messages, get_messages_backend


def generate_message() -> str:
    # TODO remove this line after 2 and 3's are done
    return str(random.choice(get_messages('1-A')))

    random_msg = random.randint(1, 3)
    if random_msg == 1:
        return str(random.choice(get_messages('1-A')))
    elif random_msg == 2:
        return str(random.choice(get_messages('2-A'))+'\n'+ str(random.choice(get_messages('2-B'))))
    else:
        return str(random.choice(get_messages('3-A'))) + '\n' + str(random.choice(get_messages('3-B')))\
             + '\n' + str(random.choice(get_messages('3-C'))) + '\n' + str(random.choice(get_messages('3-D'))) + '\n' \
             + str(random.choice(get_messages('3-E')))


def generate_message_client() -> str:
    # TODO remove this line after 2 and 3's are done
    return str(random.choice(get_messages_backend('1-A')))

    random_msg = random.randint(1, 3)
    if random_msg == 1:
        return str(random.choice(get_messages_backend('1-A')))
    elif random_msg == 2:
        return str(random.choice(get_messages_backend('2-A'))+'\n'+ str(random.choice(get_messages_backend('2-B'))))
    else:
        return str(random.choice(get_messages_backend('3-A'))) + '\n' + str(random.choice(get_messages_backend('3-B')))\
             + '\n' + str(random.choice(get_messages_backend('3-C'))) + '\n' + str(random.choice(get_messages_backend('3-D'))) + '\n' \
             + str(random.choice(get_messages_backend('3-E')))
