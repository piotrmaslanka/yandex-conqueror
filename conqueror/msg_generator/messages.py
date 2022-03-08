import random

from .definitions import get_messages, get_messages_backend


def get_msg_using_provider(provider):
    random_msg = random.randint(1, 10)
    if random_msg < 7:
        return str(random.choice(provider('1-A')))
    else:
        return str(random.choice(provider('2-A'))+'\n'+ str(random.choice(provider('2-B'))))


def generate_message() -> str:
    return get_msg_using_provider(get_messages)


def generate_message_client() -> str:
    return get_msg_using_provider(get_messages_backend)
