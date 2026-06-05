Update Entity API
-----------------------------------

.. table::

   +-------------------+-----------------------------------------------+
   | PUT               | ``/entities/{entity_id}``                     |
   +-------------------+-----------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^

Request content type should be ``application/json``.

This is a partial update — send only the fields you want to change. Any field
left out of the request keeps its current value.

List fields (``order_settings``, ``dynamic_field_list``) replace the existing
collection wholesale — to add a new item, include all existing items together
with the new one in the same request, otherwise the previous items will be
removed.

.. table::
    :width: 100%

    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | Field Name              | Data Type                                                    | Description                                       | Value                                                                              |
    +=========================+==============================================================+===================================================+====================================================================================+
    | name                    | string *(optional)*                                          | Name                                              | "updated_entity"                                                                   |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | type                    | string *(optional)*                                          | Type ID - UUID                                    | "d666a904-5739-46c0-b70a-1cd57658a3f6"                                             |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | status                  | string *(optional)*                                          | Status ID - UUID                                  | "e5e41ad2-1c46-4c3b-91cb-4cf1a82ac120"                                             |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | dynamic_field_list      | list object *(optional)*                                     | Object contains dynamic field key and value       | ``[{"key":"numberField","value": 456}]``                                           |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | order_settings          | list object *(optional)*                                     | Object contains order type id and order items.    | ``[{"order_type":"07b31501-70f9-4d4c-8eb7-3b013ebe8d62",                           |
    |                         |                                                              |                                                   | "order_items":["573806b5-f054-48a2-8043-c75a83be871e"]}]``                         |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+

.. |br| raw:: html

      <br>

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    entity_id = "<ENTITY_ID>"
    service_url = f"/engagement/entities/{entity_id}"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": "Bearer " + ACCESS_TOKEN,
    }

    # Send only the fields you want to change.
    data = {
        "name": "my_updated_entity",
        "type": "d666a904-5739-46c0-b70a-1cd57658a3f6",
        "status": "e5e41ad2-1c46-4c3b-91cb-4cf1a82ac120",
        "dynamic_field_list": [
            {"key": "numberField", "value": 456},
            {"key": "textField", "value": "updated"}
        ],
        "order_settings": [
            {
                "order_type": "07b31501-70f9-4d4c-8eb7-3b013ebe8d62",
                "order_items": ["573806b5-f054-48a2-8043-c75a83be871e"]
            }
        ]
    }

    resp = requests.put(
        EVREKA360_API_BASE_URL + service_url,
        headers=headers,
        json=data,
    )

    print("Status Code:", resp.status_code)
    print("Response Text:", resp.text)


Response
^^^^^^^^^^^^^^^^^
*Status Code:* ``200`` - Updated successfully

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

   {
       "id": "ENTITY ID STR",
       "success": true,
       "detail": {
           "message": "Successfully updated Entity"
       }
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
       "detail": "Entity not found"
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
