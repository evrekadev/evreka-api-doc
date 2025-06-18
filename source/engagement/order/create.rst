Create Order API
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | POST               | ``/orders``                               |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
If name field is not provided, name will be generated automatically.
One of the following fields must be provided: service_point_id, latitude and longitude. If both are provided, service_point_id will be used.
If any required dynamic field exists for the order type, it must be provided in the request.

``order_item_list`` and ``order_assets`` are fields dependant on the selected order type. Each order type may have different configuration, defined at :ref:`Order Settings<order_settings>`.

Under ``order_assets``, each action key like ``pick`` or ``drop`` is a list of asset types, with assets of that asset type included. For example, if you have assets 1 and 2 to be picked, but their asset types are different, you should have a two element array, one for each asset type.

.. table::
    :width: 100%

    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | Field Name              | Data Type                                                    | Description                                       | Value                                                                              |
    +=========================+==============================================================+===================================================+====================================================================================+
    | type_id                 | string *(required)*                                          | Order Type ID - UUID                              | d666a904-5739-46c0-b70a-1cd57658a3f6                                               |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | entity_id               | string *(required)*                                          | Entity ID - UUID                                  | d666a904-5739-46c0-b70a-1cd57658a3f6                                               |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | fulfillment_date        | string *(required)*                                          | Date                                              | 14.03.2024                                                                         |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | service_point_id        | string *(optional)*                                          | Service Point ID - UUID                           | d666a904-5739-46c0-b70a-1cd57658a3f6                                               |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | latitude                | float *(optional)*                                           | Latitude                                          | 30.12345                                                                           |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | longitude               | float *(optional)*                                           | Longitude                                         | -12.1234                                                                           |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | name                    | string *(optional)*                                          | Name of the order                                 | my_order                                                                           |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | order_item_list         | list object *(optional)*                                     | Object contains order item id and amount.         | ``[{"id": "bfdb675d-65b7-4e25-bfa9-b498faa545fc",                                  |
    |                         |                                                              |                                                   | "planned_quantity": 2}]``                                                          | 
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | order_assets            | dict object *(optional)*                                     | Object contains picked, dropped, collected  |br|  | ``{"pick":[{"asset_type":1,"assets":[1,2,3]},{"asset_type":2,"assets":[4,5,6]}],   |
    |                         |                                                              | assets, grouped by asset type                     | "drop":[{"asset_type":1,"assets":[7,8,9]},{"asset_type":2,"assets":[10,11,12]}]}`` | 
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | dynamic_field_list      | list object *(optional)*                                     | Object contains dynamic field key and value       | ``[{"key":"numberField","value": 123}]``                                           |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | contact_list            | list object *(optional)*                                     | List of Entity ID - UUID                          | ``["53d174bd-4db4-4623-aa98-078f55ce3948"]``                                       |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | note                    | string *(optional)*                                          | Note for the order                                | my_note                                                                            |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+


.. |br| raw:: html

      <br>

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/engagement/orders"
    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    # Data Example #1
    data = {
        "name": "",
        "type_id": "",
        "service_point_id": "",
        "entity_id": "",
        "fulfillment_date": "",
    }

    # Data Example #2
    data = {
        "name": "",
        "type_id": "",
        "service_point_id": "",
        "entity_id": "",
        "fulfillment_date": "",
        "order_item_list": [
            {
                "id": "",
                "planned_quantity": 0
            }
        ],
        "dynamic_field_list": [
            {
                "key": "dropdownField",
                "value": 0
            },
            {
                "key": "textField",
                "value": "text"
            },
            {
                "key": "numberField",
                "value": 123
            }
        ],
        "note": "my_note",
    }

    # Data Example #3
    data = {
        "name": "",
        "type_id": "",
        "service_point_id": "",
        "entity_id": "",
        "fulfillment_date": "",
        "order_item_list": [
            {
                "id": "",
                "planned_quantity": 0
            }
        ],
        "order_assets": {
            "pick": [
                {
                    "asset_type": 1,
                    "assets": [1, 2, 3]
                },
                {
                    "asset_type": 2,
                    "assets": [4, 5, 6]
                }
            ],
            "drop": [
                {
                    "asset_type": 1,
                    "assets": [7, 8, 9]
                },
                {
                    "asset_type": 2,
                    "assets": [10, 11, 12]
                }
            ]
        },
        "contact_list": [
            "53d174bd-4db4-4623-aa98-078f55ce3948"
        ],
    }

    resp = requests.post(EVREKA360_API_BASE_URL + service_url, headers=headers, json=data)
    print(resp.status_code, resp.json())

Response
^^^^^^^^^^^^^^^^^
*Status Code:* ``200`` - Retrieved successfully

*Content Type:* ``application/json``

*Body:*

.. code-block:: json 

    {
        "order_id": "ORDER ID UUID"
    }

*Status Code:* ``400`` - Bad request

*Content Type:* ``application/json``

*Body:*

.. code-block:: json


    {
        "detail":"An error occurred while creating the Order"
    }

