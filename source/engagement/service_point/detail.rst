.. raw:: pdf

   PageBreak

Service Point Detail API
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/service_points/{service_point_id}``     |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
A valid UUID is required as the Service Point ID to retrieve service point details.

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_point_id = ""
    service_url = "/engagement/service_points/" + service_point_id
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
        "id": "Service Point ID - UUID",
        "name": "Service Point Name - String",
        "address": "Service Point Address - String",
        "latitude": "Latitude - Float",
        "longitude": "Longitude - Float",
        "type_id": "Service Point Type ID - UUID",
        "type_name": "Service Point Type Name - String",
        "status_id": "Service Point Status ID - UUID",
        "dynamic": "Dynamic Field JSON",
        "linked_entities": [
            {
                "id": "Entity ID - UUID",
                "name": "Entity Name - String",
                "type_id": "Entity Type ID - UUID",
            }
        ]
    }

*Status Code:* ``404`` - Not Found
*Content Type:* ``application/json``
*Body:*

.. code-block:: json 

    {
        "detail": "Service Point not found"
    } 