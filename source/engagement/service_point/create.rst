Create Service Point API
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | POST              | ``/service_points``                        |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^

``name`` and ``type`` must be provided. 

If ``ops_service_point_id`` is provided, ``ops_service_point_name`` must be provided.

If ``ops_service_point_name`` is provided, ``ops_service_point_id`` must be provided.

.. table::
    :width: 100%

    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | Field Name              | Data Type                                                    | Description                                       | Value                                                                              |
    +=========================+==============================================================+===================================================+====================================================================================+
    | name                    | string *(required)*                                          | Name                                              | my_service_point                                                                   |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | type                    | string *(required)*                                          | Type ID - UUID                                    | d666a904-5739-46c0-b70a-1cd57658a3f6                                               |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | latitude                | float *(optional)*                                           | Latitude                                          | 30.12345                                                                           |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | longitude               | float *(optional)*                                           | Longitude                                         | -12.1234                                                                           |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | order_settings          | list object *(optional)*                                     | Object contains order type id and order items.    | ``[{"order_type":"07b31501-70f9-4d4c-8eb7-3b013ebe8d62",                           |
    |                         |                                                              |                                                   | "order_items":["573806b5-f054-48a2-8043-c75a83be871e"]}]``                         | 
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | entities                | list object *(optional)*                                     | List of Entity ID - UUID                          | ``["009f40a6-1dd5-4380-97b5-8b0d406ee45a"]``                                       |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | dynamic_field_list      | list object *(optional)*                                     | Object contains dynamic field key and value       | ``[{"key":"numberField","value": 123}]``                                          |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | ops_service_point_id    | integer *(optional)*                                         | Service Point ID in Ops Management                | 12345                                                                              |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | ops_service_point_name  | string *(optional)*                                          | Service Point Name in Ops Management              | my_ops_service_point                                                               |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | attachments             | File *(optional)*                                            | Service Point Attachments                         | my_attachment.png                                                                  |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+

.. |br| raw:: html

      <br>

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests
    import json

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/engagement/service_points"
    headers = {
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    # Data Example #1
    data = {
        "name": "",
        "type": "",
        "latitude": 0.0,
        "longitude": 0.0,
        "dynamic_field_list": json.dumps([
            {
                "key": "",
                "value": ""
            }
        ]),
        "order_settings": json.dumps([
            {
                "order_type": "",
                "order_items": []
            }
        ]),
        "entities": json.dumps([])
    }

    # Data Example #2
    data = {
        "name": "",
        "type": "",
        "latitude": 0.0,
        "longitude": 0.0,
        "dynamic_field_list": json.dumps([
            {
                "key": "",
                "value": 0
            }
        ]),
        "order_settings": json.dumps([
            {
                "order_type": "",
                "order_items": []
            }
        ]),
        "entities": json.dumps([]),
        "ops_service_id": 12345,
        "ops_service_name": ""
    }

    # File Data Example
    files = {
        "attachments": ("<file_name>", open("<file_name>", "rb"), "<file_type>")
    }

    resp = requests.post(EVREKA360_API_BASE_URL + service_url, headers=headers, data=data, files=files)
    print(resp.status_code, resp.json())

Response
^^^^^^^^^^^^^^^^^
*Status Code:* ``200`` - Retrieved successfully

*Content Type:* ``application/json``

*Body:*

.. code-block:: json 

    {
        "id": "SERVICE POINT ID UUID",
        "name": "SERVICE POINT NAME",
        "type_id": "SERVICE POINT TYPE ID UUID",
        "status_id": "SERVICE POINT STATUS ID UUID"
    }

*Status Code:* ``400`` - Bad request

*Content Type:* ``application/json``

*Body:*

.. code-block:: json


    {
        "detail":"An error occurred while creating the Service Point"
    }

