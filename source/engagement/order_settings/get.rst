Get Order Types and Items API
-----------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/order_settings``                        |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
One of the following filters must be provided in the request: ``entity_id``, ``service_point_id``. 
If none of the filters are provided, the API will return an empty list. If both filters are provided, the API will return intersection result.

.. table::

   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
   +=========================+==============================================================+===================================================+=======================================================+
   | entity_id               | string *(optional)*                                          | Entity ID - UUID                                  | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | service_point_id        | string *(optional)*                                          | Service Point ID - UUID                           | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+


Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/engagement/order_settings"
    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }
    
    # filter example #1
    #service_url += "?entity_id=d666a904-5739-46c0-b70a-1cd57658a3f6"

    # filter example #2
    #service_url += "?service_point_id=d666a904-5739-46c0-b70a-1cd57658a3f6"

    # filter example #3 #To use multiple filters, use the & character between the filters.
    #service_url += "?entity_id=d666a904-5739-46c0-b70a-1cd57658a3f6"
    #service_url += "&service_point_id=d666a904-5739-46c0-b70a-1cd57658a3f6"

    resp = requests.get(EVREKA360_API_BASE_URL + service_url, headers=headers)
    print(resp.status_code, resp.json())


Response
^^^^^^^^^^^^^^^^^
*Status Code:* ``200`` - Retrieved successfully
*Content Type:* ``application/json``
*Body:*

.. code-block:: json 

    {
        "order_types": [
            {
                "id": "Order Type ID -UUID",
                "name": "Order type name - String",
                "template_id": "Order type's template ID - UUID"
            }
        ],
        "order_items": [
            {
                "id": "Order Item ID - UUID",
                "name": "Order Item name - String",
                "order_type_id": "Order Type ID -UUID"
            }
        ]
    }
