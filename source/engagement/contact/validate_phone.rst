.. raw:: pdf

   PageBreak

Validate Phone Number API
-----------------------------------

.. table::
 
   +-------------------+--------------------------------------------+
   | POST              | ``/contacts/validate/phone``               |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
.. table::
    :width: 100%

   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
   +=========================+==============================================================+===================================================+=======================================================+
   | phone                   | string *(required)*                                          | Phone Number                                      | +1234567890                                           |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+

Example Code
^^^^^^^^^^^^^^^^^
.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    session = requests.session()

    service_url = "/engagement/contacts/validate/phone"
    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }
    data = {
        "phone": "1234567890"
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
    "detail": "The provided phone number is valid."
}

*Status Code:* ``400`` - Bad Request
*Content Type:* ``application/json``
*Body:*
.. code-block:: json
{
    "detail": "Duplicate phone error: ({phone})"
}
