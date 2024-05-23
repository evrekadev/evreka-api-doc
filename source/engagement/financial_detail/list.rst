Financial Detail List
---------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/financial_details``                     |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
'order_item_id' and 'order_type_id' are optional filter parameters that can be used to filter the order item list. 
When both are provided, only 'order_item_id' is used for filtering. None of them are provided, all order items are listed.


'entity_id' and 'service_point_id' are optional filter parameters that can be used to filter the financial detail list. 
The financial details of an item can be specified by entity or service point. When 'entity_id' or/and 'service_point_id' are provided, financial details are filtered by these parameters.

.. table::

   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
   +=========================+==============================================================+===================================================+=======================================================+
   | order_item_id           | string *(optional)*                                          | Order Item ID - UUID                              | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | order_type_id           | string *(optional)*                                          | Order Type ID - UUID                              | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | entity_id               | string *(optional)*                                          | Entity ID - UUID                                  | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | service_point_id        | string *(optional)*                                          | Service Point Type ID - UUID                      | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/engagement/financial_details"
    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }
    
    # filter example #1
    #service_url += "?order_item_id=d666a904-5739-46c0-b70a-1cd57658a3f6"
    
    # filter example #2
    #service_url += "?order_type_id=d666a904-5739-46c0-b70a-1cd57658a3f6"

    # filter example #2
    #service_url += "?entity_id=d666a904-5739-46c0-b70a-1cd57658a3f6"

    # filter example #3 
    #service_url += "?service_point_id=d666a904-5739-46c0-b70a-1cd57658a3f6"

    # filter example #5 #To use multiple filters, use the & character between the filters.
    # service_url += "?order_item_id=d666a904-5739-46c0-b70a-1cd57658a3f6" 
    # service_url += "&order_type_id=d666a904-5739-46c0-b70a-1cd57658a3f6"
    
    resp = requests.get(EVREKA360_BASE_URL + service_url, headers=headers)
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
                "order_item_id": "Order Item ID - UUID",
                "order_item_name": "Order Item name - String",
                "order_item_rules": "Text",
                "price": "Float",
                "market_share": "Float",
                "tax": "Float"
            }
        ]
    }
