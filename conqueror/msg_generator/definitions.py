from __future__ import annotations

import json
import random
import re
import typing as tp

REPL_RE = re.compile(r'\[(.*?)\]')


def get_messages(part_type: tp.Optional[str] = None) -> tp.List[MessagePiece]:
    with open('/app/resources/messages-short.json', 'r') as f_in:
        data = json.load(f_in)
    if part_type is None:
        return [MessagePiece.from_json(y) for y in data]
    else:
        return [MessagePiece.from_json(y) for y in data if y['type'] == part_type]


class MessagePiece:
    def __init__(self, msg_type: str, msg_content: str):
        self.msg_type = msg_type
        self.msg_content = msg_content

    @staticmethod
    def from_json(y: dict) -> MessagePiece:
        return MessagePiece(y['type'], y['content'])

    def __str__(self):
        def replacer(match):
            return random.choice(match.group(1).split('|'))
        return re.sub(REPL_RE, replacer, self.msg_content)
