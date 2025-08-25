.. raw:: pdf

   PageBreak

Service Point Status List
---------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/service_points/status``                 |
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

    service_url = "/engagement/service_points/status"
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
                "id": "Status ID - UUID",
                "name": "Status Name - String",
                "color": "Status Color - String",
            }
        ]
    }
