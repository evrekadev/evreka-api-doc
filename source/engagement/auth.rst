Auth
=======

This section describes how to authenticate with the Evreka 360 API.
As a first step, you need to get an access token to authenticate with the Evreka 360 API. 
The access token is valid for 24 hours. 
You need to include the access token in the Authorization header of your requests to the Evreka 360 API.
After your access token expired, you can get a new access token with the refresh token.

Get Access Token
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python


    import requests
    import json

    EVREKA360_BASE_URL = ""
    EVREKA360_API_USER= ""
    EVREKA360_API_PASS = ""
    EVREKA360_AUTH_CLIENT_ID = ""
    EVREKA360_AUTH_CLIENT_SECRET = ""

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
    auth_response_dict = json.loads(auth_response._content.decode('utf-8'))  

    access_token = auth_response_dict['access_token'] 
    print(access_token)
    refresh_token = auth_response_dict['refresh_token']
    print(refresh_token)

Refresh Access Token
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python


    import requests
    import json

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
    auth_response_dict = json.loads(auth_response._content.decode('utf-8'))  

    access_token = auth_response_dict['access_token'] 
    print(access_token)
    refresh_token = auth_response_dict['refresh_token']
    print(refresh_token)
