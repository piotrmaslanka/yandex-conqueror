from conqueror.app import app
from conqueror.cassandra import session
from conqueror.utils import as_json


@app.route('/v1/add-review/<string:login>')
@as_json
def add_review(login: str):
    """
    Mark a review as added
    ---
    parameters:
    - in: path
      name: login
      schema:
        type: string
      description: Login used to add reviews at
      required: true
    ---
    responses:
        '200':
            description: Added
    """
    resp = list(session.execute('SELECT entries FROM entries WHERE apiKey=%s', (login,)))
    if not resp:
        session.execute('INSERT INTO entries (apiKey, entries) VALUES (%s, 1)', (login, ))
    else:
        entries = resp[0][0]
        session.execute('INSERT INTO entries (apiKey, entries) VALUES (%s, %s)', (login, entries+1))
    return {}


@app.route('/v1/view-reviews')
@as_json
def view_reviews():
    """
    Get a sum of all reviews added up to this point
    ---
    responses:
        '200':
            description: OK
            content:
                application/json:
                    schema:
                        type: object
                        properties:
                            entries:
                                type: integer
                                description: All entries added
    """
    resp = session.execute('SELECT entries FROM entries')
    entries = sum(d[0] for d in resp)
    return {'entries': entries}
