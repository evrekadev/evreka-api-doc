Create Task Item API
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | POST              | ``/task_items``                            |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^

Creates a ``TaskItem`` for the requesting client. Only ``title`` is required;
all other fields fall back to model defaults.

Request content type should be ``application/json``.

.. table::
    :width: 100%

    +-----------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+
    | Field Name                  | Data Type                                                    | Description                                               | Value                                                                              |
    +=============================+==============================================================+===========================================================+====================================================================================+
    | title                       | string *(required)*                                          | Task Item title                                           | "Plastic Pickup"                                                                   |
    +-----------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+
    | item_uom                    | string *(optional, default "kg")*                            | Unit of measure                                           | "kg"                                                                               |
    +-----------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+
    | cost                        | float *(optional)*                                           | Cost per unit                                             | 1.25                                                                               |
    +-----------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+
    | ops_operation_id            | integer *(optional)*                                         | Operation ID to link this Task Item to                    | 678                                                                                |
    +-----------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+
    | description                 | string *(optional, default "")*                              | Free-form description                                     | "Curbside pickup"                                                                  |
    +-----------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+
    | default_quantity_value      | integer *(optional)*                                         | Default quantity for records                              | 1                                                                                  |
    +-----------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+
    | default_weight_value        | float *(optional)*                                           | Default weight for records                                | 10.0                                                                               |
    +-----------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+
    | quantity_item_id            | integer *(optional)*                                         | Sibling Task Item ID used for quantity                    | 11                                                                                 |
    +-----------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+
    | weight_item_id              | integer *(optional)*                                         | Sibling Task Item ID used for weight                      | 12                                                                                 |
    +-----------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+


Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/ops/task_items"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": "Bearer " + ACCESS_TOKEN,
    }

    # Minimal request
    data = {
        "title": "Plastic Pickup",
    }

    # Full request
    data = {
        "title": "Plastic Pickup",
        "item_uom": "kg",
        "cost": 1.25,
        "ops_operation_id": 678,
        "description": "Curbside pickup",
        "default_quantity_value": 1,
        "default_weight_value": 10.0,
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
        "task_item_id": 12345
    }

*Status Code:* ``400`` - Bad request

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

    {
        "detail": {
            "message": "Missing parameter(s): title"
        }
    }

*Status Code:* ``404`` - Not Found (when ``ops_operation_id`` does not exist)

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

    {
        "detail": {
            "message": "Operation 678 not found"
        }
    }
