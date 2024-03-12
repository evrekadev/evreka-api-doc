Get Service Availability Point API
^^^^^^^^^^^^^^^^^^^^^^

**Request:**

- *Method:* ``GET``
- *Headers:* ``Authorization [Bearer Token]`` *(required)*
- *Endpoint:* ``/service_availability/``
- *Parameters:*
    - ``Entity ID``: [UUID] *(optional)*
    - ``Service ID``: [UUID] *(optional)*
    - ``Order Type ID``: [UUID] *(optional)*
    - ``Start Date``: [Date] *(optional)*
    - ``End Date``: [Date] *(optional)*

**Response:**

- *Status Code:* ``200`` - Retrieved successfully
- *Content Type:* ``application/json``
- *Body:* Details of the retrieved service point in JSON format

.. code-block:: json

    {
        "available_dates": [
            {
                "dates": [],
                "operation": {
                    "id": "51",
                    "name": "Çato Operation"
                }
            }
        ]
    }
