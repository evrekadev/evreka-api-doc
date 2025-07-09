.. raw:: pdf

   PageBreak

Inbound List API
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/inbounds``                              |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
.. table::

   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
   +=========================+==============================================================+===================================================+=======================================================+
   | order_id                | string *(optional)*                                          | Order ID - UUID                                   | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | task_id                 | integer *(optional)*                                         | Task ID - Integer                                 | 123456                                                |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | parcel_id               | integer *(optional)*                                         | Parcel ID - Integer                               | 123456                                                |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | id_list                 | List[string] *(optional)*                                    | Inbound ID List                                   | [12345, 12356]                                        |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
  

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/mrf/inbounds"
    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    # pagination example
    #service_url += "?page=1&limit=10"

    # filter example #1
    #service_url += "?order_id=d666a904-5739-46c0-b70a-1cd57658a3f6"

    # filter example #2
    #service_url += "?task_id=123456"

    # filter example #3
    #service_url += "?parcel_id=123456"

    # filter example #4
    #service_url += "?id_list=[12345,12356]"

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
                "id": "Inbound ID - Integer",
                "external_id": "External ID - String",
                "name": "Inbound Name - String",
                "created_at": "Created At - ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>",
                "updated_at": "Updated At - ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>",
                "arrive": "Arrival Date - String",
                "status": {
                    "id": "Status ID - Integer",
                    "name": "Status Name - String",
                    "color": "Status Color - String"
                },
                "assigned_to": {
                    "id": "Assigned Parcel ID - Integer",
                    "name": "Assigned Parcel Name - String"
                },
                "dynamic": "Dynamic Field JSON"
            }
        ]
    }

*Status Code:* ``400`` - Bad request

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

    {
        "detail":"Inbound not found"
    }

