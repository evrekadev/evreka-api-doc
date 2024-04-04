.. raw:: pdf

   PageBreak

Entity Dynamic Field List
--------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/entities/dynamic_fields``               |
   +-------------------+--------------------------------------------+


Data Structure
^^^^^^^^^^^^^^^^^
'type_id' is used to filter the dynamic fields. If it is not provided, all dynamic fields will be returned. If it is provided, type_id will be used to filter the dynamic fields.

.. table::
    :width: 100%

    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
    +=========================+==============================================================+===================================================+=======================================================+
    | type_id                 | string *(optional)*                                          | Entity Type ID - UUID                             | 5f449429-cb53-4ffc-99f0-80be14559ea5                  |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+


Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests
    import json

    EVREKA360_BASE_URL = ""
    ACCESS_TOKEN = ""

    session = requests.session()

    service_url = "/engagement/entities/dynamic_fields"
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
        "items": [
            {
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
                "type_id": "ENTITY TYPE ID - UUID", // If type_id is provided
            }
        ]
    }
