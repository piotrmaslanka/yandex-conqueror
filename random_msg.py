import json
from random import randint
import random

with open('lingwistyka.json', 'r', encoding='utf-8') as f_in:
   f = json.load(f_in)

msg_bank = json.load(f)

def get_messages(header):
    list_of_msg = []
    for i in range (0, len(msg_bank)-1):
        if msg_bank[0]['type'] == header:
            list_of_msg.append(msg_bank[i]['content'])
    return list_of_msg

def gen_msg():
    random_msg = random.randint(1,3)
    if random_msg == 1:
        return str(random.choice(get_messages('1-A')))
    elif random_msg == 2:
        return str(random.choice(get_messages('2-A'))+'\n'+ str(random.choice(get_messages('2-B'))))
    else:
        return str(random.choice(get_messages('3-A'))) + '\n' + str(random.choice(get_messages('3-B')))\
             + '\n' + str(random.choice(get_messages('3-C'))) + '\n' + str(random.choice(get_messages('3-D'))) + '\n' +\
                    str(random.choice(get_messages('3-E')))

print(gen_msg())