
Get Order API
^^^^^^^^^^^^^^^^^

Request:

- Method: POST
- Endpoint: /order/
- Parameters: Order details in the request body (JSON format)

  Example request body:
  ::
  
    {
       .. "client_id": "5792a6d2-aa39-41bd-a63f-59c68ce1f5b9",                .. [required][string(UUID)]   
        "order_type_id": "5792a6d2-aa39-41bd-a63f-59c68ce1f5b9",            .. [required][string(UUID)]   
        "entity_id": "5792a6d2-aa39-41bd-a63f-59c68ce1f5b9",                .. [required][string(UUID)]   
        "service_point_id": "5792a6d2-aa39-41bd-a63f-59c68ce1f5b9",         .. [optional][string(UUID)]
        "latitute": "12.9715987",                                           .. [optional][string]
        "longitude": "77.594566",                                           .. [optional][string]
        "order_item_list": [
            {
                "order_item_id": "5792a6d2-aa39-41bd-a63f-59c68ce1f5b9",    .. [required][string(UUID)]   
                "planned_amount": 100,                                      .. [optional][number][default: 0]
            },
            {
                "order_item_id": "5792a6d2-aa39-41bd-a63f-59c68ce1f5b9",    .. [required][string(UUID)]   
                "planned_amount": 100,                                      .. [optional][number][default: 0]
            }
        ],
        "fulfillment_date": "2021-12-31",        .. [required][string][date],
        "note": "This is a note for the order"   .. [optional][string][max_length: 1000]
    }


Response:

- Status Code:
    - 200: Created successfully
    - 400: Bad request
    - 500: Internal server error
- Content Type: application/json
- Body: Details of the created order in JSON format

 Example response body:
  ::

    {
        "success": true,                                    .. [boolean]  
        "order_id": "5792a6d2-aa39-41bd-a63f-59c68ce1f5b9", .. [string(UUID)]
        "message": "Order created successfully"             .. [string]
    }

