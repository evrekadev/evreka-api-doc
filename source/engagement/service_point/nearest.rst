Service Points Nearest API List
---------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/service_points/nearest``                |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^

.. table::

   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
   +=========================+==============================================================+===================================================+=======================================================+
   | type_id                 | string *(optional)*                                          | Service Point Type ID - UUID                      | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | entity_id               | string *(optional)*                                          | Service Point Related Entity ID - UUID            | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | distance                | float *(optional)*                                           | Distance in meters, 500 as default, 1000 as max   | 500                                                   |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | latitude                | float *(optional)*                                           | Latitude coordinate for nearest search            | 39.925054                                             |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | longitude               | float *(optional)*                                           | Longitude coordinate for nearest search           | 32.8347499                                            |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | limit                   | int *(optional)*                                             | Service Point Limit, 50 as default, 50 as max     | 50                                                    |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/engagement/service_points/nearest?latitude=39.925054&longitude=32.8347499"
    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    # filter example: type_id
    #service_url += "?type_id=d666a904-5739-46c0-b70a-1cd57658a3f6"

    # filter example: entity_id
    #service_url += "?entity_id=d666a904-5739-46c0-b70a-1cd57658a3f6"

    # filter example: distance
    #service_url += "?distance=500"

    # filter example: limit
    #service_url += "?limit=50"

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
                "id": "Service Point ID - UUID",
                "name": "Service Point Name - String",
                "type_id": "Service Point Type - UUID",
                "type_name": "Service Point Type Name - String",
                "status_id": "Service Point Status ID - UUID",
                "address": "Service Point Address - String",
                "latitude": "Service Point Latitude - Float",
                "longitude": "Service Point Longitude - Float",
                "dynamic": "Dynamic Field JSON"
            }
        ]
    }

*Status Code:* ``404`` - Not Found
*Content Type:* ``application/json``
*Body:*

.. code-block:: json

    {
        "message": "Service Point Not Found"
    }
