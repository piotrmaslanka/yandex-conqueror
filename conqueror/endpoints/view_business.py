from conqueror.app import app
from conqueror.cassandra import session
from conqueror.utils import as_json


@app.route('/v1/view-businesses/<string:sector>')
@as_json
def get_businesses(sector: str):
    """
    Get a list of Russian businesses to post reviews for
    ---
    parameters:
    - in: path
      name: sector
      schema:
        type: string
      description: Name of Russian city in Latin alphabet
      required: true
    ---
    responses:
        '200':
            description: OK
            content:
                application/json:
                    schema:
                        type: array
                        items:
                            type: string
                            description: Business ID of the object
    """
    resp = session.execute('SELECT businessId FROM businesses WHERE sector=%s', (sector, ))
    results = []
    for datum in resp:
        results.append(datum[0])
    return results
