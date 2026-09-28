.. raw:: pdf

   PageBreak

Verify QR Code API
-----------------------------------

.. table::

   +------+----------------------+
   | POST | ``/qr_codes/verify`` |
   +------+----------------------+

Data Structure
^^^^^^^^^^^^^^^^^

If the token was created as ``single_use``, it is consumed with the first successful verification.

.. table::
   :width: 100%

   +------------+---------------------+--------------------------------------------+-------------------------+
   | Field Name | Data Type           | Description                                | Value                   |
   +============+=====================+============================================+=========================+
   | qr_token   | string *(required)* | Token read from the QR code                | eyJhbGciOiJFUzI1NiIs... |
   +------------+---------------------+--------------------------------------------+-------------------------+
   | scanned_by | string *(optional)* | Scanner identifier (device, asset or user) | SCN-0042                |
   +------------+---------------------+--------------------------------------------+-------------------------+
   | latitude   | float *(optional)*  | Latitude of the scan location              | 39.925054               |
   +------------+---------------------+--------------------------------------------+-------------------------+
   | longitude  | float *(optional)*  | Longitude of the scan location             | 32.8347499              |
   +------------+---------------------+--------------------------------------------+-------------------------+

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/qr_codes/verify"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    data = {
        "qr_token": "eyJhbGciOiJFUzI1NiIs...",
        "scanned_by": "SCN-0042",
        "latitude": 39.925054,
        "longitude": 32.8347499
    }

    resp = requests.post(EVREKA360_API_BASE_URL + service_url, headers=headers, json=data)
    print(resp.status_code, resp.json())

Response
^^^^^^^^^^^^^^^^^

*Status Code:* ``200`` - Verified successfully

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

    {
        "valid": true,
        "qr_code_id": "5b1f3c2e-8a4d-4f6b-9c1e-2d7a8b9c0e11",
        "contact_id": "d666a904-5739-46c0-b70a-1cd57658a3f6",
        "external_id": "USR-100245",
        "purpose": "drop_off",
        "verified_at": "2026-09-28T10:01:12Z",
        "expires_at": "2026-09-28T10:05:00Z"
    }

*Status Code:* ``400`` - Bad request

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

    {
        "valid": false,
        "detail": "QR_CODE_EXPIRED"
    }

Possible ``detail`` values for invalid tokens are ``QR_CODE_EXPIRED``, ``QR_CODE_ALREADY_USED``, ``QR_CODE_REVOKED`` and ``INVALID_SIGNATURE``.
