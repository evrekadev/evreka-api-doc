Authentication
=======

First of all, you need to get an access token to authenticate for Evreka 360 API via Evreka 360 Auth server.
You need to include the **Bearer Token** in the Authorization header of your requests to the Evreka 360 API.
After your access token expired, you can get a new access token with the refresh token. Evreka 360 Auth server use `OAuth 2.0 <https://oauth.net/2/>`_ protocol for authentication.

Get Access Token
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_BASE_URL = ""

    EVREKA360_AUTH_CLIENT_ID = ""
    EVREKA360_AUTH_CLIENT_SECRET = ""

    EVREKA360_API_USER= ""
    EVREKA360_API_PASS = ""

    session = requests.session()
    session.auth = (EVREKA360_AUTH_CLIENT_ID, EVREKA360_AUTH_CLIENT_SECRET)

    auth_data = {
        'username': EVREKA360_API_USER,
        'password': EVREKA360_API_PASS,
        'grant_type': 'password',
        'scope': 'profile'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    auth_response = session.post(
        EVREKA360_BASE_URL + "/auth/oauth/token",
        data=auth_data,
        headers=headers
    )
    auth_response_dict = auth_response.json()

    access_token = auth_response_dict['access_token']
    print("Access Token", access_token)
    refresh_token = auth_response_dict['refresh_token']
    print("Refresh Token", refresh_token)

Refresh Access Token
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_BASE_URL = ""

    EVREKA360_AUTH_CLIENT_ID = ""
    EVREKA360_AUTH_CLIENT_SECRET = ""

    REFRESH_TOKEN = ""

    session = requests.session()
    session.auth = (EVREKA360_AUTH_CLIENT_ID, EVREKA360_AUTH_CLIENT_SECRET)

    auth_data = {
        'grant_type': 'refresh_token',
        'refrest_token': REFRESH_TOKEN
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    auth_response = session.post(
        EVREKA360_BASE_URL + "/auth/oauth/token",
        data=auth_data,
        headers=headers
    )
    auth_response_dict = auth_response.json()

    access_token = auth_response_dict['access_token']
    print("Access Token", access_token)

    refresh_token = auth_response_dict['refresh_token']
    print("Refresh Token", refresh_token)
