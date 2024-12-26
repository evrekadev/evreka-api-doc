Asset Types by Service Point Id
-------------------------------

.. table::

   +-------------------+----------------------------------------------------+
   | GET               | ``/service_points/{service_point_id}/asset_types`` |
   +-------------------+----------------------------------------------------+

Example Code
^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_point_id = "SERVICE POINT ID"

    service_url = "/engagement/service_points/" + service_point_id + "/asset_types"
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
                "id": 1,
                "name": "Asset Type Name",
            }
        ]
    }
