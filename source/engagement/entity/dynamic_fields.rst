.. raw:: pdf

   PageBreak

Entity Dynamic Field List
-------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/entities/dynamic_fields``               |
   +-------------------+--------------------------------------------+


Data Structure
^^^^^^^^^^^^^^^^^
Entity type 'type_id' is used to filter the dynamic fields. If it is not provided, all dynamic fields will be returned.

.. table::
    :width: 100%

    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
    +=========================+==============================================================+===================================================+=======================================================+
    | type_id                 | string *(optional)*                                          | Entity Type ID - UUID                             | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+


Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/engagement/entities/dynamic_fields"
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
                "id": "Dynamic Field ID - UUID",
                "created_at": "Created At - ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>",
                "updated_at": "Updated At - ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>",
                "key": "Dynamic Field Key",
                "label": "Dynamic Field Label",
                "default_value": "Default Value",
                "field_type": "Dynamic Field Type - TEXT, NUMBER, DROPDOWN"
                "order": "Sort Order - Integer",
                "options": "Options - JSON", // If field_type is DROPDOWN
                "required": "Is Required - Boolean",
                "editable": "Is Editable - Boolean",
                "displayable": "Is Displayable - Boolean",
                "cp_user_allowed": "Is CP User Allowed - Boolean",
                "type_id": "Entity Type ID - UUID",
            }
        ]
    }
