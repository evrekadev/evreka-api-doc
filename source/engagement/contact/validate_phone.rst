.. raw:: pdf

   PageBreak

Validate Phone Number API
-----------------------------------

.. table::

   +--------+--------------------------------------------+
   | GET    | ``/contacts/validate/phone``               |
   +--------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^

.. table::
   :width: 100%

   +-------------------------+----------------------------+-------------------------------------------+---------------------+
   | Field Name              | Data Type                  | Description                               | Value               |
   +=========================+============================+===========================================+=====================+
   | phone                   | string *(required)*        | Phone number to be validated              | +1234567890         |
   +-------------------------+----------------------------+-------------------------------------------+---------------------+

Example Code
^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/contacts/validate/phone?phone=+123456789"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    response = requests.get(EVREKA360_API_BASE_URL + service_url, headers=headers)
    print(response.status_code, response.json())

Response
^^^^^^^^^

*Status Code:* ``200`` – Retrieved successfully
*Content Type:* ``application/json``
*Body:*

.. code-block:: json

    {
        "is_valid": true
    }

*Status Code:* ``400`` – Bad Request
*Content Type:* ``application/json``
*Body:*

.. code-block:: json

    {
        "is_valid": false,
        "detail": "Phone number already exists"
    }