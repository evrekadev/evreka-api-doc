.. raw:: pdf

   PageBreak

Entity Detail API
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/entities/{entity_id}``                  |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
A valid UUID is required as the Entity ID to retrieve entity details.

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    entity_id = ""
    service_url = "/engagement/entities/" + entity_id
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
        "id": "Entity ID - UUID",
        "name": "Entity Name - String",
        "type_id": "Entity Type ID - UUID",
        "type_name": "Entity Type Name - String",
        "status_id": "Entity Status ID - UUID",
        "dynamic": "Dynamic Field JSON",
        "linked_service_points": [
            {
                "id": "Service Point ID - UUID",
                "name": "Service Point Name - String",
                "type_id": "Service Point Type ID - UUID",
            }
        ]
    }

*Status Code:* ``404`` - Not Found
*Content Type:* ``application/json``
*Body:*

.. code-block:: json 

    {
        "detail": "Entity not found"
    } 