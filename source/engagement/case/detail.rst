Case Detail
----------------


.. table::

    +-------------------+------------------------------------------------------------+
    | GET               | ``/cases/{case_id}``                                       |
    +-------------------+------------------------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^

.. table::

    +-------------------+---------------------+------------------------------------------+--------------------------------------+
    | Field Name        | Data Type           | Description                              | Example                              |
    +===================+=====================+==========================================+======================================+
    | case_id           | string (required)   | Case ID (UUID)                           | d666a904-5739-46c0-b70a-1cd57658a3f6 |
    +-------------------+---------------------+------------------------------------------+--------------------------------------+

Notes
^^^^^^

    Requires a valid bearer token.

    Returns 400 if the client does not have cases enabled.

    Returns 404 if the case with the given case_id does not exist (or is deleted).

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""
    CASE_ID = "d666a904-5739-46c0-b70a-1cd57658a3f6"

    service_url = f"/engagement/cases/{CASE_ID}"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": "Bearer " + ACCESS_TOKEN,
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
        "id": "CASE ID - UUID",
        "name": "CASE NAME - STR",
        "type": {
            "id": "CASE TYPE ID - UUID",
            "name": "CASE TYPE NAME - STR"
        },
        "sub_type": {
            "id": "CASE SUB TYPE ID - UUID",
            "name": "CASE SUB TYPE NAME - STR"
        },
        "status": {
            "id": "CASE STATUS ID - UUID",
            "name": "CASE STATUS NAME - STR",
            "color": "CASE STATUS COLOR - STR"
        },
        "entity": {
            "id": "CASE ENTITY ID - UUID",
            "name": "CASE ENTITY NAME - STR"
        },
        "service_point": {
            "id": "CASE SERVICE POINT ID - UUID",
            "name": "CASE SERVICE POINT NAME - STR"
        },
        "latitude": "LATITUDE - FLOAT",
        "longitude": "LONGITUDE - FLOAT",
        "contact": {
            "id": "CASE CONTACT ID - UUID",
            "name": "CASE CONTACT NAME - STR"
        },
        "assignee": "CASE ASSIGNEE ID - INT",
        "author": "CASE AUTHOR ID - INT",
        "subject": "SUBJECT - STR",
        "description": "DESCRIPTION - STR",
        "corrective_action": "CORRECTIVE ACTION - STR",
        "created_at": "CREATE TIME - ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>",
        "updated_at": "UPDATE TIME - ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>",
        "completed_time": "COMPLETION TIME - ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>",
        "viewed_time": "VIEW TIME - ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>",
        "source": {
            "id": "CASE SOURCE ID - UUID",
            "name": "CASE SOURCE NAME - STR"
        },
        "dynamic": "DYNAMIC FIELDS - JSON",
        "task_id_list": [
            "LINKED TASK ID - INT"
        ],
        "attachments": [
            {
                "id": "MEDIA - UUID",
                "media_name": "MEDIA NAME - STR",
                "media_url": "MEDIA URL - STR"
            }
        ],
        "rate": "RATE - INT",
        "rate_note": "RATE NOTE - STR",
        "rate_viewed_time": "RATE VIEWED TIME - ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>"
    }
