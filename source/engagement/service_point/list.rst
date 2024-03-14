Entity List
----------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/service_points/``                       |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^

.. table::

   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
   +=========================+==============================================================+===================================================+=======================================================+
   | name                    | string *(optional)*                                          | Service Point Name                                | MyServicePoin                                         |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | type_id                 | string *(optional)*                                          | Service Point Type ID - UUID                      | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | *postcode               | string *(optional)*                                          | Dynamic Field Key - Value                         | 1234AB                                                |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
"*Dynamic Field is a custom field that can be added to Service Point. "key" of the dynamic field can be used as a filter."

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

   page = 1
   limit = 10
   service_url = f"/engagement/service_points/?page={page}&limit={limit}"

   # filter example #1
   # service_url += "&name=MyServicePoint"

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
                "name": "Service Point Name",
                "address": "Service Point Address",
                "latitude": "Service Point Latitude",
                "longitude": "Service Point Longitude",
                "type_id": "Service Point Type UUID",
                "type_name": "Service Point Type Name",
                "status_id": "Service Point Status UUID",
                "dynamic": "Dynamic Field JSON"
            }
        ]
    }
