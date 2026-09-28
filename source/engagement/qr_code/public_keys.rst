.. raw:: pdf

   PageBreak

QR Code Public Keys API
-----------------------------------

.. table::

   +-----+---------------------------+
   | GET | ``/qr_codes/public_keys`` |
   +-----+---------------------------+

Data Structure
^^^^^^^^^^^^^^^^^

Returns the public keys in `JWK Set <https://datatracker.ietf.org/doc/html/rfc7517>`_ format. Keys are identified by ``kid``, which is also present in the header of each token. Scanner applications can cache the keys and verify tokens offline; the cache should be refreshed when an unknown ``kid`` is received.

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/qr_codes/public_keys"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    resp = requests.get(EVREKA360_API_BASE_URL + service_url, headers=headers)
    print(resp.status_code, resp.json())

Response
^^^^^^^^^^^^^^^^^

*Status Code:* ``200`` - Retrieved successfully

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

    {
        "keys": [
            {
                "kty": "EC",
                "crv": "P-256",
                "alg": "ES256",
                "use": "sig",
                "kid": "e360-qr-1",
                "x": "f83OJ3D2xF1Bg8vub9tLe1gHMzV76e8Tus9uPHvRVEU",
                "y": "x_FEzRu9m36HLN_tue659LNpXW6pCyStikYjKIWI5a0"
            }
        ]
    }

*Status Code:* ``401`` - Unauthorized

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

    {
        "detail": "INVALID_TOKEN"
    }
