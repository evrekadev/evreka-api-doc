Client Bounds
-----------------------------------

.. table::

   +--------+---------------------------------------------+
   | GET    | ``/environment/map``                        |
   +--------+---------------------------------------------+

Data Structure
^^^^^^^^^^^^^^

``module`` must be provided as a query parameter.

.. table::
    :width: 100%

    +---------------------+--------------------------+---------------------------------------------------+
    | Field Name          | Data type                | Description                                       |
    +=====================+==========================+===================================================+
    | module              | string *(required)*      | Name of the module: engagement, ops, asset, fleet |
    +---------------------+--------------------------+---------------------------------------------------+

Example Code
^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    module = "engagement"
    # module = "ops"
    # module = "asset"
    # module = "fleet"

    service_url = "/environment/map?module=" + module
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    resp = requests.get(EVREKA360_API_BASE_URL + service_url, headers=headers)
    print(resp.status_code, resp.json())

Response
^^^^^^^^^

*Status Code:* ``200`` - Retrieved successfully

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

    {
        "tile_provider": "Esri | Google | Open Street Map",
        "bounds": {
            "north_east": {
                "lat": "Latitude - Float",
                "lon": "Longitude - Float"
            },
            "south_west": {
                "lat": "Latitude - Float",
                "lon": "Longitude - Float"
            }
        }
    }

*Status Code:* ``404`` - Not Found

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

    {
        "detail": "Module not found"
    }