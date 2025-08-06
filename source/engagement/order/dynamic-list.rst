.. raw:: pdf

   PageBreak

Order Dynamic Field List
-------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/orders/dynamic_fields``                 |
   +-------------------+--------------------------------------------+


Data Structure
^^^^^^^^^^^^^^^^^
'template_id' and 'type_id' are used to filter the dynamic fields. If both are not provided, all dynamic fields will be returned. If both are provided, type_id will be used to filter the dynamic fields.

.. table::
    :width: 100%

    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
    +=========================+==============================================================+===================================================+=======================================================+
    | template_id             | string *(optional)*                                          | Order Template ID - UUID                          | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | type_id                 | string *(optional)*                                          | Order Type ID - UUID                              | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+


Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/engagement/orders/dynamic_fields"
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
                "type_ids": ["ORDER TYPE ID - UUID", "ORDER TYPE ID - UUID"],
                "template_id": "ORDER TEMPLATE ID - UUID",
            }
        ]
    }
