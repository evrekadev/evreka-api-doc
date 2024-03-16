Auth
=======

This section describes how to authenticate with the Evreka 360 API.
As a first step, you need to get an access token to authenticate with the Evreka 360 API. 
The access token is valid for 30 minutes. 
You need to include the access token in the Authorization header of your requests to the Evreka 360 API.

.. code-block:: python


    import requests
    import json

    EVREKA360_BASE_URL = ""
    EVREKA360_API_USER= ""
    EVREKA360_API_PASS = ""

    session = requests.session()
    session.auth = (EVREKA360_API_USER, EVREKA360_API_PASS)

    auth_data = {
        'username': EVREKA360_API_USER,
        'password': EVREKA360_API_PASS
    }
    auth_response = session.post(EVREKA360_BASE_URL + "/token", data=auth_data)
    auth_response_dict = json.loads(auth_response._content.decode('utf-8'))  

    access_token = auth_response_dict['access_token'] 
    print(access_token)