import json
import random


def get_random_object_type() -> str:
    with open('/app/resources/object_types.json', 'r') as f_in:
        return random.choice(json.load(f_in))

