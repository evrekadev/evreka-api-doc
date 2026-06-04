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
            "name": "string"
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
            "assignee_type": "\"vehicle\" or \"employee\", nullable",
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

The ``route`` object is populated only when the task is linked to a route.
``assignee_type`` is ``"vehicle"`` when the route's assignee is a vehicle (the
``vehicle`` object is filled and ``employee`` is ``null``), or ``"employee"``
when the assignee is an employee (the ``employee`` object is filled and
``vehicle`` is ``null``).

*Status Code:* ``404`` - Not Found
*Content Type:* ``application/json``
*Body:*

.. code-block:: json 

    {
        "detail": "Task ({task_id}) not found"
    }
