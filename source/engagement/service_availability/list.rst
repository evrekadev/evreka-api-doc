
List Service Availability Point API
^^^^^^^^^^^^^^^^^^^^^^

Request:

- Method: GET
- Headers: Authorization [Bearer Token][required]
- Endpoint: /service_availability/
- Parameters: 
    - page: [int] [optional] [default: 1]
    - limit: [int] [optional] [default: 100]
    - Entity ID: [UUID] [optional]
    - Service ID: [UUID] [optional]
    - Order Type ID: [UUID] [optional]
Response:

- Status Code: 200 Retrived successfully
- Content Type: application/json
- Body: Details of the retrieved service point in JSON format
.. code-block:: python 
    {
        "items": [
            {
                "id": "UUID",
                "name": "Service Point Name",
                "address": "Service Point Address",
                "latitude": "Service Point Latitude",
                "longitude": "Service Point Longitude"
            },
            {
                "id": "UUID",
                "name": "Service Point Name",
                "address": "Service Point Address",
                "latitude": "Service Point Latitude",
                "longitude": "Service Point Longitude"
            }
        ]
    }
