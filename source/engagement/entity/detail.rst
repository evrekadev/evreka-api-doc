
Get Entity API
^^^^^^^^^^^^^^^^^^^^^^

Request:

- Method: GET
- Headers: Authorization [Bearer Token][required]
- Endpoint: /entity/{entity_id}
- Parameters: entity_id [UUID][required]

Response:

- Status Code: 200 Retrived successfully
- Content Type: application/json
- Body: Details of the retrieved entity in JSON format
.. code-block:: python
    {
        "id": "UUID",
        "name": "Entity Name",
        "type": "Entity Type UUID",
    }


