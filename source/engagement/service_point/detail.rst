
Get Service Point API
^^^^^^^^^^^^^^^^^^^^^^

Request:

- Method: GET
- Headers: Authorization [Bearer Token][required]
- Endpoint: /service_point/{service_point_id}
- Parameters: service_point_id [UUID][required]

Response:

- Status Code: 200 Retrived successfully
- Content Type: application/json
- Body: Details of the retrieved service point in JSON format
.. code-block:: python
    {
        "id": "UUID",
        "name": "Service Point Name",
        "address": "Service Point Address",
        "latitude": "Service Point Latitude",
        "longitude": "Service Point Longitude"
    }


