Change Service Point Default Items API
----------------------------------------

.. table::

   +-------------------+------------------------------------------------------------------+
   | POST              | ``/service_points/{service_point_id}/default_items``             |
   +-------------------+------------------------------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^

Overwrites the default Task Items on a single Service Point, identified by
``service_point_id`` in the URL path. The endpoint always replaces the current
default items with the list sent in the request, so send the full, final state
every time. Only Task Items whose operation belongs to the Service Point's
operations are applied.

The request is processed synchronously — a ``200`` response means the default
items on the Service Point were updated.

Request content type should be ``application/json``.

.. table::
    :width: 100%

    +----------------------+------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------+
    | Field Name           | Data Type                                                  | Description                                              | Value                                                                              |
    +======================+============================================================+==========================================================+====================================================================================+
    | default_item_list    | list of integer                                            | Task Item IDs that should become the complete set of     | ``[12345, 12346]``                                                                 |
    |                      |                                                            | default items on the target Service Point. The existing  |                                                                                    |
    |                      |                                                            | default items are replaced with this list. An empty list |                                                                                    |
    |                      |                                                            | clears all default items.                                |                                                                                    |
    +----------------------+------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------+


Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_point_id = 101
    service_url = f"/ops/service_points/{service_point_id}/default_items"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": "Bearer " + ACCESS_TOKEN,
    }

    # Overwrite the default Task Items on the Service Point with the given list
    data = {
        "default_item_list": [12345, 12346],
    }

    # Clear all default Task Items on the Service Point
    data = {
        "default_item_list": [],
    }

    resp = requests.post(EVREKA360_API_BASE_URL + service_url, headers=headers, json=data)
    print(resp.status_code, resp.json())


Response
^^^^^^^^^^^^^^^^^

*Status Code:* ``200`` - Updated successfully

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

    {
        "service_point_id": 101
    }

*Status Code:* ``400`` - Bad request

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

    {
        "detail": {
            "message": "Some task items not found"
        }
    }

*Status Code:* ``404`` - Not Found

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

    {
        "detail": {
            "message": "Service point not found: 101"
        }
    }
