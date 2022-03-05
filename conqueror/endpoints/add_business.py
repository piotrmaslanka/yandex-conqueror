from flask import request

from conqueror.app import app
from conqueror.cassandra import session
from conqueror.utils import as_json


@app.route('/v1/add-businesses')
@as_json
def add_business():
    """
    Adds a business
    ---
    requestBody:
        content:
            application/json:
                schema:
                    type: array
                    items:
                        type: object
                        properties:
                            businessId:
                                type: string
                                description: Business ID
                            sector:
                                type: string
                                description: Business' sector
    responses:
        '201':
            description: Business added
    """
    data = request.get_json()

    for datum in data:
        businessId = datum['businessId']
        sector = datum['sector']

        session.execute('INSERT INTO businesses (businessId, sector) VALUES (%s, %s)',
                        (businessId, sector))
    return {}, 201
