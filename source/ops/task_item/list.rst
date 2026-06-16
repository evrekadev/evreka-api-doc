Task Item List
------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/task_items``                            |
   +-------------------+--------------------------------------------+

Returns the active task items that belong to the authenticated client. Results
are ordered by ``id`` descending and are paginated.

Data Structure
^^^^^^^^^^^^^^^^^


.. table::
    :width: 100%

    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
    +=========================+==============================================================+===================================================+=======================================================+
    | title                   | String *(optional)*                                          | Case-insensitive filter on the task item title    | Plastic                                               |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | operation_id            | Integer *(optional)*                                         | Filter by the linked Operation ID                 | 678                                                   |
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
    title = "Plastic"
    operation_id = 678
    service_url = f"/ops/task_items"

    # filter example #1: default filter
    #service_url = "service_url"

    # filter example #2: filter with title
    #service_url += f"?title={title}"

    # filter example #3: filter with operation_id and pagination
    #service_url += f"?operation_id={operation_id}&page={page}&limit={limit}"


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
                "id": "Task Item ID - Integer",
                "title": "Task Item title - String",
                "item_uom": "Unit of measure - String, nullable",
                "cost": "Cost per unit - Float, nullable",
                "operation_id": "Linked Operation ID - Integer, nullable",
                "description": "Free-form description - String, nullable",
                "default_quantity_value": "Default quantity - Integer, nullable",
                "default_weight_value": "Default weight - Float, nullable",
                "quantity_item_id": "Sibling Task Item ID used for quantity - Integer, nullable",
                "weight_item_id": "Sibling Task Item ID used for weight - Integer, nullable",
                "active": "Whether the task item is active - Boolean"
            }
        ]
    }

*Status Code:* ``404`` - Not Found
*Content Type:* ``application/json``
*Body:*

.. code-block:: json

    {
        "detail": "Task item not found"
    }
