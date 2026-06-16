Service Point List
------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/service_points``                        |
   +-------------------+--------------------------------------------+

Returns the active service points that belong to the authenticated client.
Results are ordered by ``id`` descending and are paginated.

Data Structure
^^^^^^^^^^^^^^^^^


.. table::
    :width: 100%

    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
    +=========================+==============================================================+===================================================+=======================================================+
    | name                    | String *(optional)*                                          | Case-insensitive filter on the service point name | Main Depot                                            |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | type                    | String *(optional)*                                          | Case-insensitive filter on the service point type | default                                               |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | operation_id            | Integer *(optional)*                                         | Only service points linked to this Operation      | 678                                                   |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | region_id               | Integer *(optional)*                                         | Only service points linked to this Region         | 316                                                   |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | page                    | Integer *(optional)*                                         | Page number (default 1)                           | 1                                                     |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | limit                   | Integer *(optional)*                                         | Items per page (default 10, max 50)               | 10                                                    |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    page = 1
    limit = 10
    name = "Main Depot"
    type = "default"
    operation_id = 678
    region_id = 316
    service_url = f"/ops/service_points"

    # filter example #1: default filter
    #service_url = "service_url"

    # filter example #2: filter with name
    #service_url += f"?name={name}"

    # filter example #3: filter with type and pagination
    #service_url += f"?type={type}&page={page}&limit={limit}"

    # filter example #4: filter with operation and region
    #service_url += f"?operation_id={operation_id}&region_id={region_id}"


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
                "id": "Service Point ID - Integer",
                "name": "Service Point name - String",
                "type": "Service Point type - String",
                "latitude": "Latitude - Float",
                "longitude": "Longitude - Float",
                "time_window_start": "Time window start - String (HH:MM), nullable",
                "time_window_end": "Time window end - String (HH:MM), nullable",
                "default_items": [
                    {
                        "id": "Task Item ID - Integer",
                        "name": "Task Item title - String, nullable"
                    }
                ],
                "operations": [
                    {
                        "id": "Operation ID - Integer",
                        "name": "Operation name - String, nullable"
                    }
                ],
                "regions": [
                    {
                        "id": "Region ID - Integer",
                        "name": "Region name - String, nullable"
                    }
                ]
            }
        ]
    }

*Status Code:* ``404`` - Not Found
*Content Type:* ``application/json``
*Body:*

.. code-block:: json

    {
        "detail": "Service point not found"
    }
