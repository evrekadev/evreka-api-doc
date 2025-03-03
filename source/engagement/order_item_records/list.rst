Order Item Records List
-----------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/order_item_records``                    |
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
    service_url = f"/engagement/order_item_records?page={page}&limit={limit}&order_id={order_id}"

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
                "id": "Order Item Record ID - UUID",
                "name": "Order Item Record Name - String",
                "created_at": "Created At - ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>",
                "updated_at": "Updated At - ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>"
                "planned_quantity_of_primary_uom": "Planned Quantity of Primary UOM - Float",
                "actual_quantity_of_primary_uom": "Actual Quantity of Primary UOM - Float",
                "order_item_id": "Order Item ID - UUID",
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
                }
            }
        ]
    }


*Status Code:* ``404`` - Not Found
*Content Type:* ``application/json``
*Body:*

.. code-block:: json 

    {
        "detail": "Order ({order_id}) not found"
    }
