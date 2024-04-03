Entity Details
----------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/entities/{entity_id}``                  |
   +-------------------+--------------------------------------------+

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests
    import json

    EVREKA360_BASE_URL = ""
    ACCESS_TOKEN = ""
    ENTITY_ID = ""

    session = requests.session()

    service_url = f"/engagement/entities/{ENTITY_ID}"
    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    response = session.get(EVREKA360_BASE_URL + service_url, headers=headers)
    response_dict = json.loads(response._content.decode('utf-8'))
    print(response_dict)  

Response
^^^^^^^^^^^^^^^^^
*Status Code:* ``200`` - Retrieved successfully
*Content Type:* ``application/json``
*Body:*

.. code-block:: json 

    {
        "id": "UUID",
        "name": "Entity Name",
        "type_id": "Entity Type UUID",
        "type_name": "Entity Type Name",
        "status_id": "Entity Status UUID",
        "dynamic": "Dynamic Field JSON",
        "linked_service_points": [
            {
                "id": "UUID",
                "name": "Service Point Name",
                "type_id": "Service Point Type UUID"
            }
        ]
    }
