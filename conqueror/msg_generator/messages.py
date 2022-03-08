import random

from .definitions import get_messages, get_messages_backend


def get_msg_using_provider(provider):
    return str(random.choice(provider('1-A')))


def generate_message() -> str:
    return get_msg_using_provider(get_messages)


def generate_message_client() -> str:
    return get_msg_using_provider(get_messages_backend)
