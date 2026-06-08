.. raw:: pdf

   PageBreak

Task Detail API
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/tasks/{task_id}``                       |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
A valid integer is required as the Task ID to retrieve task details.

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    task_id = ""
    service_url = "/ops/tasks/" + task_id
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
        "id": "integer",
        "create_time": "ISO datetime string or null",
        "operation": {
            "id": "integer",
            "name": "string",
            "assignee_type": "\"vehicle\" or \"employee\""
        },
        "task_template": {
            "id": "integer",
            "name": "string"
        },
        "operation_date": "YYYY-MM-DD or null",
        "due_date": "YYYY-MM-DD or null",
        "shift": {
            "id": "integer",
            "name": "string"
        },
        "time_window": "object or null",
        "note": "string or null",
        "route": {
            "id": "integer",
            "name": "string or null",
            "vehicle": {
                "id": "integer",
                "name": "Vehicle plate - string, nullable"
            },
            "employee": {
                "id": "integer",
                "name": "Driver name - string, nullable"
            }
        },
        "status": {
            "id": "integer",
            "name": "string",
            "state": "string"
        },
        "service_point": {
            "id": "integer",
            "name": "string"
        },
        "location": {
            "latitude": "float",
            "longitude": "float"
        },
        "source": "object or null"
    }

The ``route`` object is populated only when the task is linked to a route. Its
``vehicle`` and ``employee`` objects are each filled independently when the
route's assignee has a vehicle and/or an employee; either one is ``null`` when
the corresponding assignee is not set.

*Status Code:* ``404`` - Not Found
*Content Type:* ``application/json``
*Body:*

.. code-block:: json 

    {
        "detail": "Task ({task_id}) not found"
    }
