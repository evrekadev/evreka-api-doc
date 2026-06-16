Order Item List
------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/order_items``                           |
   +-------------------+--------------------------------------------+

Returns the order items that belong to the authenticated client. Results are
ordered by ``id`` descending and are paginated.

Data Structure
^^^^^^^^^^^^^^^^^


.. table::
    :width: 100%

    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
    +=========================+==============================================================+===================================================+=======================================================+
    | name                    | String *(optional)*                                          | Case-insensitive filter on the order item name    | Plastic                                               |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | order_type_id           | UUID *(optional)*                                            | Filter by the linked Order Type ID                | 0b1d...                                               |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | page                    | Integer *(optional)*                                         | Page number (default 1)                           | 1                                                     |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | limit                   | Integer *(optional)*                                         | Items per page (default 10, max 50)               | 10                                                    |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    page = 1
    limit = 10
    name = "Plastic"
    order_type_id = "0b1d6c3e-1234-5678-9abc-def012345678"
    service_url = f"/engagement/order_items"

    # filter example #1: default filter
    #service_url = "service_url"

    # filter example #2: filter with name
    #service_url += f"?name={name}"

    # filter example #3: filter with order_type_id and pagination
    #service_url += f"?order_type_id={order_type_id}&page={page}&limit={limit}"


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
                "id": "Order Item ID - UUID",
                "name": "Order Item name - String",
                "order_type_id": "Linked Order Type ID - UUID",
                "primary_uom": "Primary unit of measure - String",
                "secondary_uom": "Secondary unit of measure - String, nullable",
                "cost_per_unit_primary_uom": "Cost per unit of primary UOM - Float, nullable",
                "point_per_unit_primary_uom": "Points per unit of primary UOM - Float, nullable",
                "is_adjustable": "Whether the quantity is adjustable - Boolean (default false)",
                "mappings": [
                    {
                        "ops_operation_id": "Linked OPS operation ID - Integer, nullable",
                        "task_item_id": "Linked OPS task item ID - Integer, nullable",
                        "material_id": "Linked MRF material ID - Integer, nullable"
                    }
                ]
            }
        ]
    }

The ``mappings`` array is empty when the order item has no mapping. Each mapping
carries a ``task_item_id`` or a ``material_id`` (optionally with ``ops_operation_id``).

*Status Code:* ``404`` - Not Found
*Content Type:* ``application/json``
*Body:*

.. code-block:: json

    {
        "detail": "Order item not found"
    }
