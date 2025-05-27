Validate Email API
-----------------------------------

.. table::

   +--------+--------------------------------------------+
   | GET    | ``/contacts/validate/email``               |
   +--------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^

.. table::
   :width: 100%

   +-------------------------+----------------------------+-------------------------------------------+-------------------------+
   | Field Name              | Data Type                  | Description                               | Value                   |
   +=========================+============================+===========================================+=========================+
   | email                   | string *(required)*        | Email address to be validated             | example@gmail.com       |
   +-------------------------+----------------------------+-------------------------------------------+-------------------------+

Example Code
^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/contacts/validate/email?email=example@gmail.com"
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
        "detail": "Email already exists"
    }