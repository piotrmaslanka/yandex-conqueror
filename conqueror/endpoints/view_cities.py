from conqueror.app import app
from conqueror.scraper.data_reader import read_cities
from conqueror.utils import as_json


@app.route('/v1/view-cities')
@as_json
def get_cities():
    """
    Get a list of Russian cities
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
                            type: object
                            properties:
                                name:
                                    type: string
                                    description: Name of the city in Latin
                                population:
                                    type: integer
                                    description: Population of the city
                            required:
                                - name
                                - population
    """
    cities = read_cities()
    results = []
    for city in cities:
        results.append({'name': city.city_in_english,
                        'population': city.population})
    return results

