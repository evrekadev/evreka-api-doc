Create Order Item API
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | POST              | ``/order_items``                           |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^

Creates an ``OrderItem`` under the given ``order_type``. If both
``ops_task_item_id`` and ``ops_operation_id`` are provided, an
``OrderItemMapping`` linking the new ``OrderItem`` to the Ops Task Item is
written in the same transaction. If neither is provided, only the
``OrderItem`` is created. The pair must be provided together — supplying just
one returns ``400``.

Request content type should be ``application/json``.

.. table::
    :width: 100%

    +-----------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+
    | Field Name                  | Data Type                                                    | Description                                               | Value                                                                              |
    +=============================+==============================================================+===========================================================+====================================================================================+
    | order_type                  | string *(required)*                                          | Order Type ID - UUID                                      | "d666a904-5739-46c0-b70a-1cd57658a3f6"                                             |
    +-----------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+
    | name                        | string *(required)*                                          | Order Item name                                           | "Plastic Waste"                                                                    |
    +-----------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+
    | primary_uom                 | string *(optional, default "kg")*                            | Primary unit of measure                                   | "kg"                                                                               |
    +-----------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+
    | secondary_uom               | string *(optional)*                                          | Secondary unit of measure                                 | "ton"                                                                              |
    +-----------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+
    | cost_per_unit_primary_uom   | float *(optional)*                                           | Cost per primary unit                                     | 1.25                                                                               |
    +-----------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+
    | point_per_unit_primary_uom  | float *(optional)*                                           | Points awarded per primary unit                           | 0.5                                                                                |
    +-----------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+
    | ops_task_item_id            | integer *(optional)*                                         | Ops Task Item ID — must be sent with ``ops_operation_id`` | 12345                                                                              |
    |                             |                                                              | to create an ``OrderItemMapping``                         |                                                                                    |
    +-----------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+
    | ops_operation_id            | integer *(optional)*                                         | Ops Operation ID — must be sent with ``ops_task_item_id`` | 678                                                                                |
    |                             |                                                              | to create an ``OrderItemMapping``                         |                                                                                    |
    +-----------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+
    | material_id                 | integer *(optional)*                                         | MRF Material ID to link this Order Item to                | 42                                                                                 |
    +-----------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+


Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/engagement/order_items"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": "Bearer " + ACCESS_TOKEN,
    }

    # Order Item only
    data = {
        "order_type": "d666a904-5739-46c0-b70a-1cd57658a3f6",
        "name": "Plastic Waste",
        "primary_uom": "kg",
        "cost_per_unit_primary_uom": 1.25,
        "point_per_unit_primary_uom": 0.5,
    }

    # Order Item + Order Item Mapping (link to an existing Ops Task Item)
    data = {
        "order_type": "d666a904-5739-46c0-b70a-1cd57658a3f6",
        "name": "Plastic Waste",
        "primary_uom": "kg",
        "cost_per_unit_primary_uom": 1.25,
        "point_per_unit_primary_uom": 0.5,
        "ops_task_item_id": 12345,
        "ops_operation_id": 678,
        "material_id": 42,
    }

    resp = requests.post(EVREKA360_API_BASE_URL + service_url, headers=headers, json=data)
    print(resp.status_code, resp.json())


Response
^^^^^^^^^^^^^^^^^

*Status Code:* ``200`` - Created successfully

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

    {
        "order_item_id": "ORDER ITEM ID UUID"
    }

*Status Code:* ``400`` - Bad request

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

    {
        "detail": {
            "message": "ops_task_item_id and ops_operation_id must be provided together"
        }
    }

*Status Code:* ``404`` - Not Found

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

    {
        "detail": {
            "message": "Order type not found"
        }
    }
