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
Task ID is integer ID for the task to retrieve details.

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
        "name": "string",
        "description": "string or null",
        "order": "integer",
        "service_type": "string",
        "is_required": "boolean",
        "assets": [
            {
                "name": "string",
                "items": [
                    {
                        "item_id": "integer",
                        "item_name": "string",
                        "quantity": "float or null",
                        "amount": "float or null",
                        "actual_quantity": "float or null",
                        "actual_amount": "float or null",
                        "uom": "string or null"
                    }
                ],
                "tare_weight": "float or null"
            }
        ],
        "form": [
            {
                "label": "string",
                "value": "string",
                "type": "string",
                "json_value": "form_value_json",
                "options": "form_options"
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
