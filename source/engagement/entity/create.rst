Create Entity API
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | POST              | ``/entities``                              |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^

``name`` and ``type`` must be provided.

Request content type should be multipart/form-data.

.. table::
    :width: 100%

    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | Field Name              | Data Type                                                    | Description                                       | Value                                                                              |
    +=========================+==============================================================+===================================================+====================================================================================+
    | name                    | string *(required)*                                          | Name                                              | my_entity                                                                          |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | type                    | string *(required)*                                          | Type - UUID                                       | d666a904-5739-46c0-b70a-1cd57658a3f6                                               |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | order_settings          | list object *(optional)*                                     | Object contains order type id and order items.    | ``[{"order_type":"07b31501-70f9-4d4c-8eb7-3b013ebe8d62",                           |
    |                         |                                                              |                                                   | "order_items":["573806b5-f054-48a2-8043-c75a83be871e"]}]``                         |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | dynamic_field_list      | list object *(optional)*                                     | Object contains dynamic field key and value       | ``[{"key":"numberField","value": 123"}]``                                          |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | attachments             | file *(optional)*                                            | A list of files uploaded via multipart/form-data  | ``my_attachment.png``                                                              |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+

.. |br| raw:: html

      <br>

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import json
    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""
    service_url = "/engagement/entities"
    headers = {
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    data = {
        "name": "Sample Name",
        "type": "UUID",
        "dynamic_field_list": json.dumps([
            {"key": "sample-df-1", "value": 1},
            {"key": "sample-df-2", "value": "19.02.2025"},
            {"key": "sample-df-3", "value": "test"}
        ]),
        "order_settings": json.dumps([
            {"order_type": "UUID", "order_items": ["UUID"]},
            {"order_type": "UUID",
             "order_items": ["UUID"]}])
    }

    files = [
        ('attachments', ('sample.jpg', open('<path-to-sample.jpg>', 'rb'), 'image/jpeg')),
        ('attachments', ('sample2.jpg', open('<path-to-sample2.jpg>', 'rb'), 'image/jpeg')),
        ('attachments', ('sample3.jpg', open('<path-to-sample3.jpg>', 'rb'), 'image/jpeg'))
    ]

    resp = requests.post(
        EVREKA360_API_BASE_URL + service_url,
        headers=headers,
        data=data,  # Sending as form-data
        files=files  # Attachments
    )

    print("Status Code:", resp.status_code)
    print("Response Text:", resp.text)


Response
^^^^^^^^^^^^^^^^^
*Status Code:* ``200`` - Retrieved successfully

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

   {
       "id": "ENTITY ID STR",
       "success": "RESPONSE STATUS BOOL",
       "detail": "RESPONSE CONTAINING MESSAGE OBJECT DICT"
   }

*Status Code:* ``400`` - Bad request

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

   {
       "detail": {
           "message": "An error occurred while creating the Entity"
       }
   }

