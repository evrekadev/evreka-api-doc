Service Point Details
-----------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/service_points/{service_point_id}``     |
   +-------------------+--------------------------------------------+

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests
    import json

    EVREKA360_BASE_URL = ""
    ACCESS_TOKEN = ""
    SERVICE_POINT_ID = ""

    session = requests.session()

    service_url = f"/engagement/service_points/{SERVICE_POINT_ID}"
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
        "name": "Service Point Name",
        "address": "Service Point Address",
        "latitude": "Service Point Latitude",
        "longitude": "Service Point Longitude",
        "type_id": "Service Point Type UUID",
        "type_name": "Service Point Type Name",
        "status_id": "Service Point Status UUID",
        "dynamic": "Dynamic Field JSON",
        "linked_entities": [
            {
                "id": "Linked Entity UUID",
                "name": "Linked Entity Name",
                "type_id": "Linked Entity Type UUID"
            }
        ]
    }
