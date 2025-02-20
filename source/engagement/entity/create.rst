Create Entity API
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | POST              | ``/entity``                                |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^

``name`` and ``type_id`` must be provided.

.. table::
    :width: 100%

    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | Field Name              | Data Type                                                    | Description                                       | Value                                                                              |
    +=========================+==============================================================+===================================================+====================================================================================+
    | name                    | string *(required)*                                          | Name                                              | my_service_point                                                                   |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | type_id                 | string *(required)*                                          | Type ID - UUID                                    | d666a904-5739-46c0-b70a-1cd57658a3f6                                               |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | order_settings          | list object *(optional)*                                     | Object contains order type id and order items.    | ``[{"order_type":"07b31501-70f9-4d4c-8eb7-3b013ebe8d62",                           |
    |                         |                                                              |                                                   | "order_items":["573806b5-f054-48a2-8043-c75a83be871e"]}]``                         |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | dynamic_field_list      | list object *(optional)*                                     | Object contains dynamic field key and value       | ``[{"key":"numberField","value": 123"}]``                                          |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | attachments             | list of files *(optional)*                                   | A list of files uploaded via multipart/form-data  | ``["file1.jpg", "file2.pdf"]``                                                     |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+

.. |br| raw:: html

      <br>

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

   import requests
   EVREKA360_API_BASE_URL = ""
   ACCESS_TOKEN = ""
   service_url = "/engagement/entity"
   headers = {
       "Content-Type": "multipart/form-data; boundary=<>",
       "Authorization": "Bearer " + ACCESS_TOKEN
   }
   # Data Example

    data = {
        "name": "Sample Name",
        "type_id": "123e4567-e89b-12d3-a456-426614174000",
        "dynamic_field_list": '[{"key":"some_key", "value": 10}]',
        "order_settings": '[{"order_type":"type_1", "order_items":[]}]',
    }

    files = [
        ("attachments", ("file1.jpg", open("file1.jpg", "rb"), "image/jpg")),
        ("attachments", ("file2.jpeg", open("file2.jpeg", "rb"), "image2/jpeg")),
    ]

   resp = requests.post(EVREKA360_API_BASE_URL + service_url, headers=headers, json=data)
   print(resp.status_code, resp.json())

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

