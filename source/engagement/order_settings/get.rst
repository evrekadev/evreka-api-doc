Get Order Types and Items API
^^^^^^^^^^^^^^^^^

**Request:**

- *Method:* ``GET``
- *Headers:* ``Authorization [Bearer Token]`` *(required)*
- *Endpoint:* ``/order_settings/``
- *Parameters:*
    - ``Entity ID``: [UUID] *(optional)*
    - ``Service Point ID``: [UUID] *(optional)*

**Response:**

- *Status Code:* ``200`` - Retrieved successfully
- *Content Type:* ``application/json``
- *Body:* Details of the retrieved order in JSON format

.. code-block:: json

    {
        "order_types": [
            {
                "id": "UUID",
                "name": "String",
                "order_items": [
                    {
                        "id": "UUID",
                        "name": "String"
                    }
                ]
            }
        ]
    }
