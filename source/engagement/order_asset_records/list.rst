Order Asset Records List
-----------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/order_asset_records``                   |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
``order_id`` must be provided as a query parameter.

.. table::
    :width: 100%

    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
    +=========================+==============================================================+===================================================+=======================================================+
    | order_id                | string *(required)*                                          | Order ID - UUID                                   | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    page = 1
    limit = 10
    order_id = "ORDER_ID_UUID"
    service_url = f"/engagement/order_asset_records?page={page}&limit={limit}&order_id={order_id}"

    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    resp = requests.get(EVREKA360_API_BASE_URL + service_url, headers=headers)
    print(resp.status_code, resp.json())

Response
^^^^^^^^^^^^^^^^^

*Status Code:* ``200`` - Retrieved successfully
*Content Type:* ``application/json``
*Body:*

.. code-block:: json
    {
        "items": [
        {
            "id": "Order Asset Record ID - UUID",
            "order": "Order Name - String",
            "asset_action": "Asset Action - String",
            "order_assets": [
                {
                    "id": Order Asset ID - Integer,
                    "name": "Order Asset Name - String"
                }
            ],
            "order_asset_type": {
                "id": Asset Type ID - Integer,
                "name": "Asset Type Name - String"
            },
            "is_collected": "Is Collected - Boolean",
            "unit_price": {
                "value": "Unit Price - Float",
                "currency": "Currency - String"
            },
            "market_share": "Market Share - Float",
            "tax": {
                "value": "Tax - Float",
                "currency": "Currency - String"
            },
            "total_actual_price": {
                "value": "Total Actual Price - Float",
                "currency": "Currency - String"
            },
            "created_at": "Created At - ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>",
            "updated_at": "Updated At - ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>"
        },
        ]
    }


*Status Code:* ``404`` - Not Found
*Content Type:* ``application/json``
*Body:*

.. code-block:: json 

    {
        "detail": "Order ({order_id}) not found"
    }