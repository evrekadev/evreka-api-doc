Asset Financial Detail List
---------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/asset_financial_details``               |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
``asset_type_id`` is an optional filter parameter that can be used to filter the asset type list. 

``order_type_id`` is an optional filter parameter that can be used to filter the order type list. 

``entity_id`` and ``service_point_id`` are optional filter parameters that can be used to filter the asset financial detail list. 
The financial details of an asset type can be specified by entity or service point. When 'entity_id' or/and 'service_point_id' are provided, asset financial details are filtered by these parameters.

.. table::

   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
   +=========================+==============================================================+===================================================+=======================================================+
   | asset_type_id           | int *(optional)*                                             | Asset Type ID - int                               | 1                                                     |
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

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/engagement/asset_financial_details"
    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }
    
    # filter example #1
    # service_url += "?asset_type_id=1"
    
    # filter example #2
    # service_url += "?entity_id=d666a904-5739-46c0-b70a-1cd57658a3f6"

    # filter example #3 
    # service_url += "?service_point_id=d666a904-5739-46c0-b70a-1cd57658a3f6"

    # filter example #4
    # To use multiple filters, use the & character between the filters.
    # service_url += "?asset_type_id=1" 
    # service_url += "&entity_id=d666a904-5739-46c0-b70a-1cd57658a3f6"
    
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
                "asset_type": "Order Item ID - UUID",
                "price": "Float",
                "market_share": "Float",
                "tax": "Float"
            }
        ]
    }
