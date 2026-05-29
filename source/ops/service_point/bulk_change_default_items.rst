Bulk Change Service Point Default Items API
---------------------------------------------

.. table::

   +-------------------+--------------------------------------------------------+
   | POST              | ``/service_points/bulk_change_default_items``          |
   +-------------------+--------------------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^

Adds, removes, or overwrites the default Task Items on a set of Service Points.
The set is either an explicit ``id_list`` of Service Point IDs, or *all* Service
Points the caller can see (when ``select_all`` is ``true``, with optional
``filters`` applied upstream).

The request is processed asynchronously upstream — a successful response only
means the job was accepted.

Request content type should be ``application/json``.

.. table::
    :width: 100%

    +----------------------+------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------+
    | Field Name           | Data Type                                                  | Description                                              | Value                                                                              |
    +======================+============================================================+==========================================================+====================================================================================+
    | mode                 | string *(required)*                                        | One of ``"add"``, ``"remove"``, ``"overwrite"``          | "add"                                                                              |
    +----------------------+------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------+
    | select_all           | boolean *(optional, default false)*                        | When ``true``, target every Service Point matching       | false                                                                              |
    |                      |                                                            | ``filters``; ``id_list`` is then ignored                 |                                                                                    |
    +----------------------+------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------+
    | id_list              | list of integer *(required when select_all is false)*      | Service Point IDs to update                              | ``[101, 102, 103]``                                                                |
    +----------------------+------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------+
    | default_item_list    | list of integer *(required for "add" and "remove")*        | Task Item IDs to add to / remove from / overwrite the    | ``[12345, 12346]``                                                                 |
    |                      |                                                            | default items on the target Service Points               |                                                                                    |
    +----------------------+------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------+
    | filters              | list *(optional, only used with select_all)*               | Column-manager filter expressions applied upstream       | ``[]``                                                                             |
    |                      |                                                            | when resolving "all" Service Points                      |                                                                                    |
    +----------------------+------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------+


Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/ops/service_points/bulk_change_default_items"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": "Bearer " + ACCESS_TOKEN,
    }

    # Add default Task Items to specific Service Points
    data = {
        "mode": "add",
        "id_list": [101, 102, 103],
        "default_item_list": [12345, 12346],
    }

    # Overwrite default Task Items on every Service Point matching filters
    data = {
        "mode": "overwrite",
        "select_all": True,
        "default_item_list": [12345],
        "filters": [],
    }

    # Remove default Task Items from specific Service Points
    data = {
        "mode": "remove",
        "id_list": [101, 102],
        "default_item_list": [12346],
    }

    resp = requests.post(EVREKA360_API_BASE_URL + service_url, headers=headers, json=data)
    print(resp.status_code, resp.json())

All Possible ``filters`` Entries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each entry is ``{"key": "<column key>", "value": <value>}``. Date range values
are two-element lists in ``DD.MM.YYYY`` format. Unknown / unfilterable keys are
silently ignored upstream.

.. code-block:: python

    filters = [
        # Service Point ID — integer "starts with" match
        {"key": "id", "value": 101},

        # Active flag — boolean
        {"key": "is_active", "value": True},

        # Name — text contains
        {"key": "name", "value": "Main Depot"},

        # Service Point type — one of: default, special_needs, vip, caution
        {"key": "type", "value": "default"},

        # Creation date — [start, end] in DD.MM.YYYY
        {"key": "create_datetime", "value": ["01.01.2026", "31.01.2026"]},

        # Last update date — [start, end] in DD.MM.YYYY
        {"key": "last_update_time", "value": ["01.01.2026", "31.01.2026"]},

        # Operations — list of Operation IDs (multi-select)
        {"key": "operations", "value": [678, 679]},

        # Regions — list of Region IDs (multi-select)
        {"key": "regions", "value": [12, 14]},

        # Dynamic field — use the dynamic field's key as the filter key.
        # The value type depends on the dynamic field's own type
        # (text / number / dropdown value / multi-dropdown values list).
        {"key": "my_dynamic_text_field", "value": "some text"},
        {"key": "my_dynamic_number_field", "value": 5},
        {"key": "my_dynamic_dropdown_field", "value": "option_value"},
        {"key": "my_dynamic_multi_dropdown_field", "value": ["opt_a", "opt_b"]},
    ]

    data = {
        "mode": "overwrite",
        "select_all": True,
        "default_item_list": [12345],
        "filters": filters,
    }

    resp = requests.post(EVREKA360_API_BASE_URL + service_url, headers=headers, json=data)
    print(resp.status_code, resp.json())


Response
^^^^^^^^^^^^^^^^^

*Status Code:* ``200`` - Job accepted

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

    {
        "success": true,
        "detail": {
            "message": "İsteğiniz işleniyor."
        }
    }

*Status Code:* ``400`` - Bad request

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

    {
        "detail": {
            "message": "mode must be one of: add, remove, overwrite"
        }
    }

*Status Code:* ``404`` - Not Found

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

    {
        "detail": {
            "message": "No service points found"
        }
    }
