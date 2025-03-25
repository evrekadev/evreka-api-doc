.. raw:: pdf

   PageBreak

Step Detail API
-----------------------------------

.. table::

   +-------------------+------------------------------------------------------------------+
   | GET               | ``/tasks/{task_id}/transitions/{transition_id}/steps/{step_id}`` |
   +-------------------+------------------------------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
Task ID is integer ID for the step to retrieve details.
Transition ID is integer ID for the step to retrieve details.
Step ID is integer ID for the step to retrieve details.

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    task_id = ""
    transition_id = ""
    step_id = ""
    service_url = f"/ops/tasks/{task_id}/transitions/{transition_id}/steps/{step_id}"
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
                "type": "text" | "email" | "phone" | "email" | "dropdown",
            }
            {
                "label": "string",
                "value": "float",
                "type": "number",
            }
            {
                "label": "string",
                "value": ["string"],
                "type": "multiple_dropdown" | "image"
            }
            {
                "label": "string",
                "value": "boolean",
                "type": "checkbox",
            }
            {
                "label": "string",
                "value": "",
                "type": "checkbox",
            }
            {
                "label": "string",
                "value": "UTC ISO Date",
                "type": "date",
            }
        ]
    }

*Status Code:* ``404`` - Not Found
*Content Type:* ``application/json``
*Body:*

.. code-block:: json 

    {
        "detail": "Step ({step_id}) not found"
    } 