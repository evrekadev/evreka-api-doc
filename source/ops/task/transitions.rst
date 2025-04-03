.. raw:: pdf

   PageBreak

Task Transitions API
-----------------------------------

.. table::

   +-------------------+------------------------------------------------+
   | GET               | ``/tasks/{task_id}/transitions``               |
   +-------------------+------------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
Task ID is integer ID for the task to retrieve transitions.

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    task_id = ""
    service_url = "/ops/tasks/" + task_id + "/transitions"
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
                "id": "integer",  
                "task_status_category": {
                    "id": "integer",  
                    "name": "string",  
                    "state": "string" 
                },
                "start_time": "datetime",  
                "end_time": "datetime",  
                "user": {
                    "id": "integer",  
                    "name": "string"  
                }, 
                "next_transitions": ["integer"],  
                "steps": ["integer"],  
                "latitude": "float or null",  
                "longitude": "float or null"  
            }
        ]
    }

*Status Code:* ``404`` - Not Found
*Content Type:* ``application/json``
*Body:*

.. code-block:: json 

    {
        "detail": "Task ({task_id}) not found"
    } 