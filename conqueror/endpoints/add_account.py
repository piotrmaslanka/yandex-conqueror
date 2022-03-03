from conqueror.app import app


@app.route('/v1/add-yandex-account')
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
                        login:

                    $ref: '#/definitions/UserWithPasswordWithoutLogin'

    """