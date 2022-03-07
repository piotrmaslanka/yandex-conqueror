from flask import request

from conqueror.app import app
from conqueror.cassandra import session
from conqueror.utils import as_json


@app.route('/v1/add-businesses', methods=['PUT'])
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
                            lat:
                                type: float
                                description: Geographical latitude in degrees. + is North
                            lon:
                                type: float
                                description: Geographical longitude in degrees. + is East
                            name:
                                type: string
                                description: Optional object name
                        required:
                            - businessId
                            - sector
    responses:
        '201':
            description: Business added
    """
    data = request.get_json()

    for datum in data:
        businessId = datum['businessId']
        sector = datum['sector']
        lat = datum.get('lat')
        lon = datum.get('lon')
        name = datum.get('name')

        session.execute('INSERT INTO businesses (businessId, sector, GeoLat, geoLon, name) VALUES (%s, %s, %s, %s, %s)',
                        (businessId, sector, lat, lon, name))
        session.execute('INSERT INTO sectors (sector) VALUES (%s)', (sector,))
    return {}, 201
