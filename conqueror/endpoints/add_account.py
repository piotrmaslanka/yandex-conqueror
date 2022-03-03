from flask import request

from conqueror.app import app
from conqueror.cassandra import session
from conqueror.utils import as_json


@app.route('/v1/add-yandex-account', methods=['PUT'])
@as_json
def add_yandex_account():
    """
    Add a Yandex account
    ---
    requestBody:
        content:
            application/json:
                schema:
                    type: object
                    properties:
                        email:
                            type: string
                            format: email
                            description: User's email
                        password:
                            type: string
                            format: password
                            description: User's password
    responses:
        '201':
            description: Account added
    """
    data = request.get_json()
    email = data['email']
    password = data['password']

    session.execute('INSERT INTO accounts (email, password, status) VALUES (%s, %s, %s)',
                    (email, password, 0))
    return {}, 201
