.. raw:: pdf

   PageBreak

Create QR Code API
-----------------------------------

.. table::

   +------+---------------+
   | POST | ``/qr_codes`` |
   +------+---------------+

Data Structure
^^^^^^^^^^^^^^^^^

One of fields ``contact_id`` or ``external_id`` must be provided.

.. table::
   :width: 100%

   +-------------+---------------------+--------------------------------------------------+--------------------------------------+
   | Field Name  | Data Type           | Description                                      | Value                                |
   +=============+=====================+==================================================+======================================+
   | contact_id  | string *(optional)* | Contact ID - UUID                                | d666a904-5739-46c0-b70a-1cd57658a3f6 |
   +-------------+---------------------+--------------------------------------------------+--------------------------------------+
   | external_id | string *(optional)* | Contact ID in the client system                  | USR-100245                           |
   +-------------+---------------------+--------------------------------------------------+--------------------------------------+
   | expires_in  | int *(optional)*    | Validity in seconds, 300 as default, 900 as max  | 300                                  |
   +-------------+---------------------+--------------------------------------------------+--------------------------------------+
   | single_use  | bool *(optional)*   | Token can be verified only once, true as default | true                                 |
   +-------------+---------------------+--------------------------------------------------+--------------------------------------+
   | purpose     | string *(optional)* | Usage context of the token                       | drop_off                             |
   +-------------+---------------------+--------------------------------------------------+--------------------------------------+

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/qr_codes"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    data = {
        "external_id": "USR-100245",
        "expires_in": 300,
        "single_use": True,
        "purpose": "drop_off"
    }

    resp = requests.post(EVREKA360_API_BASE_URL + service_url, headers=headers, json=data)
    print(resp.status_code, resp.json())

Response
^^^^^^^^^^^^^^^^^

*Status Code:* ``201`` - Created successfully

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

    {
        "qr_code_id": "5b1f3c2e-8a4d-4f6b-9c1e-2d7a8b9c0e11",
        "qr_token": "eyJhbGciOiJFUzI1NiIsImtpZCI6ImUzNjAtcXItMSJ9...",
        "contact_id": "d666a904-5739-46c0-b70a-1cd57658a3f6",
        "external_id": "USR-100245",
        "issued_at": "2026-09-28T10:00:00Z",
        "expires_at": "2026-09-28T10:05:00Z"
    }

*Status Code:* ``400`` - Bad request

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

    {
        "detail": "CONTACT_NOT_FOUND"
    }
