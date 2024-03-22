.. raw:: pdf

   PageBreak

Order Status List
---------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/orders/status``                         |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
There is no required parameter for this request.

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests
    import json

    EVREKA360_BASE_URL = ""
    ACCESS_TOKEN = ""

    session = requests.session()

    service_url = "/engagement/orders/status"
    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    response = session.get(EVREKA360_BASE_URL + service_url, headers=headers)
    response_dict = json.loads(response._content.decode('utf-8'))
    print(response_dict) 

Response
^^^^^^^^^^^^^^^^^
*Status Code:* ``200`` - Retrieved successfully
*Content Type:* ``application/json``
*Body:*

.. code-block:: json

    {
        "items": [
            {
                "id": "Status ID - UUID",
                "name": "Status Name"
            }
        ]
    }
