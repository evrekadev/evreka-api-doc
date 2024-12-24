Assets by Service Point Id
-----------------------

.. table::

   +-------------------+------------------------------------------------+
   | GET               | ``/service_points/{service_point_id}/assets``  |
   +-------------------+------------------------------------------------+

Data Structure
^^^^^^^^^^^^^^

.. table::

   +--------------------+-------------------+----------------------------------+
   | Field              | Data Type         | Description                      |
   +====================+===================+==================================+
   | asset_type_id      | int *(optional)*  | Filters assets by type           |
   +--------------------+-------------------+----------------------------------+

Example Code
^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_point_id = "SERVICE POINT ID"

    service_url = "/engagement/service_points/" + service_point_id + "/assets"

    # filter example
    # service_url += "?asset_type_id=1"

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
                "name": "Asset Name",
                "type_id": 1,
            }
        ]
    }
