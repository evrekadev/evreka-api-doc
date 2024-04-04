.. raw:: pdf

   PageBreak

Service Point Dynamic Field List
---------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/service_points/dynamic_fields``         |
   +-------------------+--------------------------------------------+


Data Structure
^^^^^^^^^^^^^^^^^
'type_id' is used to filter the dynamic fields. If it is not provided, all dynamic fields will be returned. If it is provided, type_id will be used to filter the dynamic fields.

.. table::
    :width: 100%

    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
    +=========================+==============================================================+===================================================+=======================================================+
    | type_id                 | string *(optional)*                                          | Service Point Type ID - UUID                      | dc4ac5d7-f33e-46eb-90b7-73dedeb50dce                  |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+


Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests
    import json

    EVREKA360_BASE_URL = ""
    ACCESS_TOKEN = ""

    session = requests.session()

    service_url = "/engagement/service_points/dynamic_fields"
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
                "type_id": "SERVICE POINT TYPE ID - UUID", // If type_id is provided
            }
        ]
    }
