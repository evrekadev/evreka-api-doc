Inbound Outage List
-----------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/mrf/inbounds/outages``                  |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
There is no required parameter for this request.

Example Code
^^^^^^^^^^^^^^^^^
.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/mrf/inbounds/outages"
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
        "items": [
            {
                "id": "Outage ID - Integer",
                "name": "Outage Name - String",
            }
        ],
        "types": [
            {
                "value": "Outage Type ID - Integer",
                "label": "Outage Type Name - String",
            }
        ]
    }
