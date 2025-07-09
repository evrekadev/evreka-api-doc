Get Service Availability Point API V2
--------------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | POST              | ``/v2/engagement/service_availability``    |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^

If the ``end_date`` is not provided, the ``end_date`` will be set as end of the year.

If ``include_routes`` is not provided, it will be set to ``false`` by default, and the response will include routes for each date in the specified range.

``order_type_id`` and ``order_type_ids`` should not be provided together. Only one of them should be provided. If none of them is provided, all order types will be considered.

.. table::

   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
   +=========================+==============================================================+===================================================+=======================================================+
   | start_date              | string *(required)*                                          | Start Date of date range                          | 2024-03-01                                            |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | -end_date               | string *(optional)*                                          | End Date of date range                            | 2024-03-01                                            |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | entity_id               | string *(optional)*                                          | Entity ID - UUID                                  | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | service_point_id        | string *(optional)*                                          | Service Point ID - UUID                           | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | order_type_id           | string *(optional)*                                          | Order Type ID - UUID                              | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | order_type_ids          | list of strings *(optional)*                                 | Order Type IDs - UUIDs                            | ["d666a904-5739-46c0-b70a-1cd57658a3f6"]              |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | include_routes          | boolean *(optional)*                                         | Include routes in the response - Boolean          | true                                                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/v2/engagement/service_availability"
    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }
    # Data Example #1
    data = {
        "start_date": "2024-02-03",
        "end_date": "2024-03-30",
        "include_routes": False,
    }

    # Data Example #2
    data = {
        "start_date": "",
        "end_date": "",
        "entity_id": "", 
        "service_point_id": "",
        "order_type_id": ""   
    }

    resp = requests.post(EVREKA360_API_BASE_URL + service_url, headers=headers, json=data)
    print(resp.status_code, resp.json())

Response
^^^^^^^^^^^^^^^^^
*Status Code:* ``200`` - Retrieved successfully
*Content Type:* ``application/json``
*Body:*

.. code-block:: json 

    {
        "dates": [
            {
                "date": "2024-08-28T00:00:00",
                "routes": [
                    {
                        "value": 110,
                        "label": "Route Order # 1",
                        "model": "RouteOrder",
                        "op_id": 1
                    }
                ],
                "order_types": [ 
                    {
                        "order_type_id": "Order Type ID - UUID",
                        "order_type_name": "Order Type Name - String",
                    }
                ],
            }
        ]
    }
    
