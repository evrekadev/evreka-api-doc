Update Service Point API
-----------------------------------

.. table::

   +-------------------+-----------------------------------------------+
   | PATCH             | ``/service_points/{service_point_id}``        |
   +-------------------+-----------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^

Request content type should be ``application/json``.

This is a partial update — send only the fields you want to change. Any field
left out of the request keeps its current value.

List fields (``order_settings``, ``dynamic_field_list``, ``entities``,
``contact_list``) replace the existing collection wholesale — to add a new item,
include all existing items together with the new one in the same request,
otherwise the previous items will be removed.

Pairing rules:

* ``latitude`` and ``longitude`` must be provided together (both or neither).
* ``ops_service_point_id`` and ``ops_service_point_name`` must be provided together.

.. table::
    :width: 100%

    +----------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | Field Name                 | Data Type                                                    | Description                                       | Value                                                                              |
    +============================+==============================================================+===================================================+====================================================================================+
    | name                       | string *(optional)*                                          | Name                                              | "updated_service_point"                                                            |
    +----------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | type                       | string *(optional)*                                          | Type ID - UUID                                    | "d666a904-5739-46c0-b70a-1cd57658a3f6"                                             |
    +----------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | status                     | string *(optional)*                                          | Status ID - UUID                                  | "e5e41ad2-1c46-4c3b-91cb-4cf1a82ac120"                                             |
    +----------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | latitude                   | float *(optional)*                                           | Latitude                                          | 30.54321                                                                           |
    +----------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | longitude                  | float *(optional)*                                           | Longitude                                         | -12.5432                                                                           |
    +----------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | address                    | string *(optional)*                                          | Address                                           | "123 Example St, Example City"                                                     |
    +----------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | dynamic_field_list         | list object *(optional)*                                     | Object contains dynamic field key and value       | ``[{"key":"numberField","value": 456}]``                                           |
    +----------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | order_settings             | list object *(optional)*                                     | Object contains order type id and order items.    | ``[{"order_type":"07b31501-70f9-4d4c-8eb7-3b013ebe8d62",                           |
    |                            |                                                              |                                                   | "order_items":["573806b5-f054-48a2-8043-c75a83be871e"]}]``                         |
    +----------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | entities                   | list object *(optional)*                                     | List of Entity ID - UUID                          | ``["009f40a6-1dd5-4380-97b5-8b0d406ee45a"]``                                       |
    +----------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | contact_list               | list object *(optional)*                                     | List of Contact ID - UUID                         | ``["abf8c97a-9a43-4232-a8ff-5d6a4d87c021"]``                                       |
    +----------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | ops_service_point_id       | integer *(optional)*                                         | Service Point ID in Ops Management                | 12345                                                                              |
    +----------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | ops_service_point_name     | string *(optional)*                                          | Service Point Name in Ops Management              | "ops_service_point_updated"                                                        |
    +----------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+


Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_point_id = "<SERVICE_POINT_ID>"
    service_url = f"/engagement/service_points/{service_point_id}"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": "Bearer " + ACCESS_TOKEN,
    }

    # Send only the fields you want to change.
    data = {
        "name": "my_updated_service_point",
        "type": "d666a904-5739-46c0-b70a-1cd57658a3f6",
        "status": "e5e41ad2-1c46-4c3b-91cb-4cf1a82ac120",
        "latitude": 30.54321,
        "longitude": -12.5432,
        "address": "123 Example St, Example City",
        "dynamic_field_list": [
            {"key": "numberField", "value": 456}
        ],
        "order_settings": [
            {
                "order_type": "07b31501-70f9-4d4c-8eb7-3b013ebe8d62",
                "order_items": ["573806b5-f054-48a2-8043-c75a83be871e"]
            }
        ],
        "entities": ["009f40a6-1dd5-4380-97b5-8b0d406ee45a"],
        "contact_list": ["abf8c97a-9a43-4232-a8ff-5d6a4d87c021"],
        "ops_service_point_id": 12345,
        "ops_service_point_name": "my_ops_service_point_updated"
    }

    resp = requests.patch(EVREKA360_API_BASE_URL + service_url, headers=headers, json=data)
    print(resp.status_code, resp.json())


Response
^^^^^^^^^^^^^^^^^
*Status Code:* ``200`` - Updated successfully

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

    {
        "id": "SERVICE POINT ID UUID"
    }

*Status Code:* ``400`` - Bad request

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

    {
        "detail": "Invalid JSON format in '<field_name>'."
    }

*Status Code:* ``404`` - Not Found

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

    {
        "detail": "Service Point ({service_point_id}) not found"
    }

*Status Code:* ``422`` - Unprocessable Entity

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

    {
        "detail": [
            {
                "loc": ["<field>"],
                "msg": "<validation error message>",
                "type": "value_error"
            }
        ]
    }
