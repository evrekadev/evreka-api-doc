Update Entity API
-----------------------------------

.. table::

   +-------------------+-----------------------------------------------+
   | PUT               | ``/entities/{entity_id}``                     |
   +-------------------+-----------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^

Request content type should be ``multipart/form-data``.

All existing data on the entity must be re-sent in the request to maintain it.
List fields (``order_settings``, ``dynamic_field_list``) replace the existing
collection wholesale — to add a new item, include all existing items together
with the new one in the same request, otherwise the previous items will be
removed.

For attachments, existing files are preserved unless their IDs are listed in
``attachments_tbd``; any files sent in ``attachments`` are added on top.

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
    | attachments             | file *(optional)*                                            | New files to upload via multipart/form-data       | ``my_attachment.png``                                                              |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | attachments_tbd         | list object *(optional)*                                     | List of existing attachment IDs (UUID) to delete  | ``["009f40a6-1dd5-4380-97b5-8b0d406ee45a"]``                                       |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+

.. |br| raw:: html

      <br>

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import json
    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    entity_id = "<ENTITY_ID>"
    service_url = f"/engagement/entities/{entity_id}"
    headers = {
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    data = {
        "name": "my_updated_entity",
        "type": "d666a904-5739-46c0-b70a-1cd57658a3f6",
        "status": "e5e41ad2-1c46-4c3b-91cb-4cf1a82ac120",
        "dynamic_field_list": json.dumps([
            {"key": "numberField", "value": 456},
            {"key": "textField", "value": "updated"}
        ]),
        "order_settings": json.dumps([
            {
                "order_type": "07b31501-70f9-4d4c-8eb7-3b013ebe8d62",
                "order_items": ["573806b5-f054-48a2-8043-c75a83be871e"]
            }
        ]),
        "attachments_tbd": json.dumps(["009f40a6-1dd5-4380-97b5-8b0d406ee45a"])
    }

    files = [
        ("attachments", ("sample.jpg", open("<path-to-sample.jpg>", "rb"), "image/jpeg")),
    ]

    resp = requests.put(
        EVREKA360_API_BASE_URL + service_url,
        headers=headers,
        data=data,
        files=files,
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
       },
       "entity_type": "ENTITY TYPE ID UUID",
       "entity_name": "ENTITY NAME",
       "entity_external_id": "ENTITY EXTERNAL ID"
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
