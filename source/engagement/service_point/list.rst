
List Service Point API
^^^^^^^^^^^^^^^^^^^^^^

Request:

- Method: GET
- Headers: Authorization [Bearer Token][required]
- Endpoint: /service_point/
- Parameters: 
    - page: [int] [optional] [default: 1]
    - limit: [int] [optional] [default: 100]
    - {field_name}: [string] [optional] [default: '']

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
