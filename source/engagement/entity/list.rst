Entity List
----------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/entity/``                               |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^

.. table::
   :width: 100%

   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
   +=========================+==============================================================+===================================================+=======================================================+
   | name                    | string *(optional)*                                          | Entity Name                                       | MyEntity                                              |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | type_id                 | string *(optional)*                                          | Entity Type ID - UUID                             | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | *postcode               | string                                                       | Dynamic Field Key - Value                         | 1234AB                                                |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
"*Dynamic Field is a custom field that can be added to Entity. "key" of the dynamic field can be used as a filter."


Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

   page = 1
   limit = 10
   service_url = f"/engagement/entity/?page={page}&limit={limit}"

   # filter example #1
   # service_url += "&name=MyEntity"

   # filter example #2
   # service_url += "&type=d666a904-5739-46c0-b70a-1cd57658a3f6"

   # filter example #3 
   # service_url += "&postcode=1234AB"

   headers = {"Content-Type": "application/json; charset=utf-8"}

   resp = session.get(EVREKA360_BASE_URL + service_url, headers=headers)

Response
^^^^^^^^^^^^^^^^^
    *Status Code:* ``200`` - Retrieved successfully
    *Content Type:* ``application/json``
    *Body:*

.. code-block:: json 

    {
        "items": [
            {
                "id": "UUID",
                "name": "Entity Name",
                "type_id": "Entity Type UUID",
                "type_name": "Entity Type Name",
                "dynamic": "Dynamic Field JSON"
            }
        ]
    }
