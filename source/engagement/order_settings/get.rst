.. _order_settings:

Get Order Types and Items API
-----------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/order_settings``                        |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
One of the following filters must be provided in the request: ``entity_id``, ``service_point_id``. 
If none of the filters are provided, the API will return an empty list. If both filters are provided, the API will return intersection result.
Both ``entity_id`` and ``service_point_id`` can be single UUIDs or UUID lists.


.. table::

   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
   +=========================+==============================================================+===================================================+=======================================================+
   | entity_id               | list[str] *(optional)*                                       | Entity ID List - UUID                             | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | service_point_id        | list[str] *(optional)*                                       | Service Point ID List- UUID                       | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | include_points          | bool *(optional)*                                            | Include Points - Boolean                          | true or false                                         |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+

Enum Definitions
^^^^^^^^^^^^^^^^^

.. table::

   +-------------------+-------------------------------------------------------------------+-----------------------------------------------------+
   | Name              | Values                                                            | Description                                         |
   +===================+===================================================================+=====================================================+
   | item_selection    | ``none`` ``optional`` ``required``                                | Defines requirement of order item selection |br|    |
   |                   |                                                                   | when creating an order with an order type.          |
   +-------------------+-------------------------------------------------------------------+-----------------------------------------------------+
   | asset_selection   | ``no_asset_item`` ``pick`` ``drop`` ``collect`` ``pick_and_drop`` | Defines requirement of asset selection |br|         |
   |                   |                                                                   | when creating an order with an order type.          |
   +-------------------+-------------------------------------------------------------------+-----------------------------------------------------+

.. |br| raw:: html

      <br>

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/engagement/order_settings"
    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }
    
    # filter example #1
    #service_url += "?entity_id=d666a904-5739-46c0-b70a-1cd57658a3f6"
    #service_url += "&include_points=true"

    # filter example #2
    #service_url += "?service_point_id=d666a904-5739-46c0-b70a-1cd57658a3f6"
    #service_url += "&include_points=true"

    # filter example #3 #To use multiple filters, use the & character between the filters.
    #service_url += "?entity_id=d666a904-5739-46c0-b70a-1cd57658a3f6"
    #service_url += "&service_point_id=d666a904-5739-46c0-b70a-1cd57658a3f6"
    #service_url += "&include_points=true"

    # filter example #4 #To send multiple ids, use the , character between the ids.
    #service_url += "?entity_id=d666a904-5739-46c0-b70a-1cd57658a3f6,d666a904-5739-46c0-b70a-1cd57658a3f6"
    #service_url += "&include_points=true"

    # filter example #5 #To send multiple ids, use the , character between the ids.
    #service_url += "?service_point_id=d666a904-5739-46c0-b70a-1cd57658a3f6,d666a904-5739-46c0-b70a-1cd57658a3f6"
    #service_url += "&include_points=true"

    resp = requests.get(EVREKA360_API_BASE_URL + service_url, headers=headers)
    print(resp.status_code, resp.json())


Response
^^^^^^^^^^^^^^^^^
*Status Code:* ``200`` - Retrieved successfully
*Content Type:* ``application/json``
*Body:*

.. code-block:: json 

    {
        "order_types": [
            {
                "id": "Order Type ID -UUID",
                "name": "Order type name - String",
                "template_id": "Order type's template ID - UUID",
                "item_selection": "Item selection - String",
                "asset_selection": "Asset selection - String",
            }
        ],
        "order_items": [
            {
                "id": "Order Item ID - UUID",
                "name": "Order Item name - String",
                "order_type_id": "Order Type ID -UUID"
                "points_per_uom": "Points per Unit Primary UOM - Float",
                "primary_uom": "Primary UOM - String",
                "secondary_uom": "Secondary UOM - String or null",
                "uom_type": {
                    "value": "UOM Type value - Integer",
                    "label": "UOM Type label - String"
                }
            }
        ]
    }
