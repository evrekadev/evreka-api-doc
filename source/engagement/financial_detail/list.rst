Financial Detail List
---------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/financial_detail/``                     |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
'order_item_id' and 'order_type_id' are optional filter parameters that can be used to filter the order item list. 
When both are provided, only 'order_item_id' is used for filtering. None of them are provided, all order items are listed.


'entity_id' and 'service_point_id' are optional filter parameters that can be used to filter the financial detail list. 
The financial details of an item can be specified by entity or service point. When 'entity_id' or/and 'service_point_id' are provided, financial details are filtered by these parameters.

.. table::
   :width: 100%

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

   page = 1
   limit = 10
   service_url = f"/engagement/financial_detail/?page={page}&limit={limit}"

   # filter example #1
   # service_url += "&order_item_id=d666a904-5739-46c0-b70a-1cd57658a3f6"
   
   # filter example #1.2
   # service_url += "&order_type_id=d666a904-5739-46c0-b70a-1cd57658a3f6"

   # filter example #2
   # service_url += "&entity_id=d666a904-5739-46c0-b70a-1cd57658a3f6"

   # filter example #3 
   # service_url += "&service_point_id=d666a904-5739-46c0-b70a-1cd57658a3f6"

   headers = {"Content-Type": "application/json; charset=utf-8"}

   resp = session.get(EVREKA360_BASE_URL + service_url, headers=headers)

Response
^^^^^^^^^^^^^^^^^
    *Status Code:* ``200`` - Retrieved successfully
    *Content Type:* ``application/json``
    *Body:*

.. code-block:: json

    {
        "items": [
            {
                "order_item_id": "UUID",
                "order_item_name": "Order Item Name",
                "price": "Float",
                "market_share": "Float",
                "tax": "Float"
            }
        ]
    }
