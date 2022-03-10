from conqueror.app import app
from conqueror.msg_generator import get_messages
from conqueror.utils import as_json


@app.route('/v1/view-messages')
@as_json
def list_messages():
    """
    Return a list of messages to be sent to the Russians
    ---
    responses:
        '200':
            description: OK
            content:
                application/json:
                    schema:
                        type: array
                        items:
                            type: object
                            properties:
                                type:
                                    type: string
                                    description: 1-A
                                content:
                                    type: string
                                    example: "[Russians|People of the Russia] wake up plax!"
                                    description: Content of the message
                            required:
                                - type
                                - content
    """
    results = []
    for msg in get_messages():
        results.append({'type': msg.msg_type,
                        'content': msg.msg_content})
    return results

