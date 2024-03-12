List Entity API
^^^^^^^^^^^^^^^^^^^^^^

**Request:**

- *Method:* ``GET``
- *Headers:* ``Authorization [Bearer Token]`` *(required)*
- *Endpoint:* ``/entity/``
- *Parameters:* 
    - ``page``: [int] *(optional, default: 1)*
    - ``limit``: [int] *(optional, default: 100)*
    - ``{params}``: [string] *(optional)*

**Response:**

- *Status Code:* ``200`` - Retrieved successfully
- *Content Type:* ``application/json``
- *Body:* Details of the retrieved service point in JSON format

.. code-block:: json 

    {
        "items": [
            {
                "id": "UUID",
                "name": "Entity Name",
                "type_id": "Entity Type UUID",
                "type_name": "Entity Type Name",
                "dynamic": "Dynamic Field JSON"
            },
            {
                "id": "UUID",
                "name": "Entity Name",
                "type_id": "Entity Type UUID",
                "type_name": "Entity Type Name",
                "dynamic": "Dynamic Field JSON"
            }
        ]
    }
