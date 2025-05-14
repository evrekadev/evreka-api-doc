.. raw:: pdf

   PageBreak

Validate Contact Information API
-----------------------------------
.. table::
 
   +-------------------+--------------------------------------------+
   | GET               | ``/contacts/validate``                     |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
.. table::
    :width: 100%

    One of the following filters must be provided in the request: ``email``, ``phone``. 

   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
   +=========================+==============================================================+===================================================+=======================================================+
   | email                   | string *(optional)*                                          | Email Address                                     | example@gmail.com                                     |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | phone                   | string *(optional)*                                          | Phone Number                                      | +1234567890                                           |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+

Example Code
^^^^^^^^^^^^^^^^^
.. code-block:: python

    import requests
    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/contacts/validate"
    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }
    # Data Example #1
    email = "example@gmail.com"
    phone = "+1234567890"

    service_url+="?email="+email+"&phone="+phone
    resp = requests.get(EVREKA360_API_BASE_URL + service_url, headers=headers)
    print(resp.status_code, resp.json())


Response
^^^^^^^^^^^^^^^^^
*Status Code:* ``200`` - Retrieved successfully
*Content Type:* ``application/json``
*Body:*

.. code-block:: json
{
    "detail": "The provided information is valid."
}

*Status Code:* ``400`` - Bad Request
*Content Type:* ``application/json``
*Body (can contain one or multiple errors):*

.. code-block:: json

    {
        "detail": [
            "Duplicate phone error: {(phone)}",
            "Duplicate email error: {(email)}",
        ]
    }

