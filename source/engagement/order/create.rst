Create Order API
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | POST               | ``/orders/create``                        |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
If name field is not provided, name will be generated automatically.
One of the following fields must be provided: service_point_id, latitude and longitude. If both are provided, service_point_id will be used.
If any required dynamic field exists for the order type, it must be provided in the request.

.. table::
    :width: 100%

   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
   +=========================+==============================================================+===================================================+=======================================================+
   | type_id                 | string *(required)*                                          | Order Type ID - UUID                              | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | entity_id               | string *(required)*                                          | Entity ID - UUID                                  | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | fulfillment_date        | string *(required)*                                          | Date                                              | 14.03.2024                                            |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | service_point_id        | string *(optional)*                                          | Service Point ID - UUID                           | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | latitude                | float *(optional)*                                           | Latitude                                          | 30.12345                                              |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | longitude               | float *(optional)*                                           | Longitude                                         | -12.1234                                              |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | name                    | string *(optional)*                                          | Name of the order                                 | my_order                                              |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | order_item_list         | list object *(optional)*                                     | Object contains order item id and amount.         | [{"id": "bfdb675d-65b7-4e25-bfa9-b498faa545fc",       |
   |                         |                                                              |                                                   |     "planned_quantity": 2}]                           | 
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | dynamic_field_list      | list object *(optional)*                                     | Object contains dynamic field key and value       | [{ "key": "numberField",                              |
   |                         |                                                              |                                                   |     "value": 123": 2}]                                | 
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    service_url = f"/engagement/orders/create"
    headers = {"Content-Type": "application/json; charset=utf-8"}
    resp = session.post(EVREKA360_BASE_URL + service_url,  data=data, headers=headers)

   # post example #1
   {
        "name": "my order",
        "type_id": "d7b140e0-4ef5-42dd-a1c3-4009b190a0f4",
        "service_point_id": "1426958d-893c-4af4-9c43-7e4ac763f60f",
        "entity_id": "3c89fcd5-073f-4c9c-ba52-c0bc01ccc55f",
        "fulfillment_date": "14.03.2024",
        "order_item_list": [
            {
                "id": "bfdb675d-65b7-4e25-bfa9-b498faa545fc",
                "planned_quantity": 2
            }
        ],
        "dynamic_field_list": [
            {
                "key": "dropdownField",
                "value": 1
            },
            {
                "key": "textfield",
                "value": "  Text"
            },
            {
                "key": "numberField",
                "value": 123
            }
        ]
    }
    # post example #2
   {
        "name": "my order",
        "type_id": "d7b140e0-4ef5-42dd-a1c3-4009b190a0f4",
        "latitude": 30.12345,
        "longitude": -12.1234,
        "entity_id": "3c89fcd5-073f-4c9c-ba52-c0bc01ccc55f",
        "fulfillment_date": "14.03.2024",
    }

Response
^^^^^^^^^^^^^^^^^
*Status Code:* ``200`` - Retrieved successfully
*Content Type:* ``application/json``
*Body:*

.. code-block:: json 

    {
        "order_id": "ORDER ID UUID"
    }
    
.. code-block:: tex

Status Code:* ``400`` - Bad request
*Content Type:* ``application/json``
*Body:*

.. code-block:: json


    {
        "detail":"An error occurred while creating the Order"
    }

