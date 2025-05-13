.. raw:: pdf

   PageBreak

Validate Email Address API
-----------------------------------
.. table::
 
   +-------------------+--------------------------------------------+
   | POST              | ``/contacts/validate/email``               |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
.. table::
    :width: 100%

   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
   +=========================+==============================================================+===================================================+=======================================================+
   | email                   | string *(required)*                                          | Email Address                                     | example@gmail.com                                     |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+

Example Code
^^^^^^^^^^^^^^^^^

Example Code
^^^^^^^^^^^^^^^^^
.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    session = requests.session()

    service_url = "/engagement/contacts/validate/email"
    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }
    data = {
        "email": "example@gmail.com"
    }

    response = session.post(EVREKA360_API_BASE_URL + service_url, headers=headers, json=data)
    print(resp.status_code, resp.json())


Response
^^^^^^^^^^^^^^^^^
*Status Code:* ``200`` - Retrieved successfully
*Content Type:* ``application/json``
*Body:*

.. code-block:: json
{
    "detail": "The provided email address is valid."
}

*Status Code:* ``400`` - Bad Request
*Content Type:* ``application/json``
*Body:*
.. code-block:: json
{
    "detail": "Duplicate email error: ({email})"
}
