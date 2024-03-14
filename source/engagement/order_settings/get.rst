Get Order Types and Items API
-----------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/order_settings/``                       |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^

.. table::

   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
   +=========================+==============================================================+===================================================+=======================================================+
   | entity_id               | string *(optional)*                                          | Entity ID - UUID                                  | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | service_point_id        | string *(optional)*                                          | Service Point ID - UUID                           | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+


Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

   service_url = f"/engagement/order_settings/

   # filter example #1
   # service_url += "&entity_id=d666a904-5739-46c0-b70a-1cd57658a3f6"

   # filter example #2
   # service_url += "&service_point_id=d666a904-5739-46c0-b70a-1cd57658a3f6"


   headers = {"Content-Type": "application/json; charset=utf-8"}

   resp = session.get(EVREKA360_BASE_URL + service_url, headers=headers)

Response
^^^^^^^^^^^^^^^^^
*Status Code:* ``200`` - Retrieved successfully
*Content Type:* ``application/json``
*Body:*

.. code-block:: json 

  {
    "order_types": [
        {
            "id": "UUID",
            "name": "String",
        }
    ],
    "order_items": [
        {
            "id": "UUID",
            "name": "String",
            "order_type_id": "UUID",
        }
    ]
  }
