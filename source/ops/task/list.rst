Task List
------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/tasks``                                 |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
``order_id`` should be provided as a query parameter.

.. table::
    :width: 100%

    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
    +=========================+==============================================================+===================================================+=======================================================+
    | order_id                | UUID *(optional)*                                            | Order ID - UUID                                   | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | operation_start_date    | String *(optional)*                                          | Operation Start Date - YYYY-MM-DD                 | 2025-03-01                                            |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | operation_end_date      | String *(optional)*                                          | Operation End Date - YYYY-MM-DD                   | 2025-03-01                                            |
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
    operation_start_date = "2025-03-01"
    operation_end_date = "2025-03-01"
    service_url = f"/ops/tasks"

    # filter example #1: default filter 
    #service_url = "service_url"

    # filter example #2: filter with order_id
    #service_url += "?order_id=d666a904-5739-46c0-b70a-1cd57658a3f6"

    # filter example #3: filter with operation dates
    #service_url += f"?operation_start_date={operation_start_date}&operation_end_date={operation_end_date}"

    # filter example #4: filter with order_id and operation dates with pagination
    #service_url += f"?order_id={order_id}&operation_start_date={operation_start_date}&operation_end_date={operation_end_date}&page={page}&limit={limit}"


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
            "id": "Task ID - Integer",
            "create_time": "UTC ISO Date Time"
            "operation_date": "String Date - YYYY-MM-DD", 
            "status": {
                "id": "Status ID - Integer",
                "name": "Status Name - String",
                "state": "  Status State - String",
            }
        },
        ]
    }

*Status Code:* ``404`` - Not Found
*Content Type:* ``application/json``
*Body:*

.. code-block:: json 

    {
        "detail": "Task not found"
    }