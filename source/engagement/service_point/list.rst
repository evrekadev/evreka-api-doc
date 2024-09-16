Service Point List
-----------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/service_points``                        |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^

.. table::

   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
   +=========================+==============================================================+===================================================+=======================================================+
   | name                    | string *(optional)*                                          | Service Point Name                                | MyServicePoint                                        |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | type_id                 | string *(optional)*                                          | Service Point Type ID - UUID                      | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | entity_id               | string *(optional)*                                          | Service Point Related Entity ID - UUID            | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | order_types             | list[str] *(optional)*                                       | Order By Type IDs                                 | ``["d666a904-5739-46c0-b70a-1cd57658a3f6"]``          |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | order_items             | list[str] *(optional)*                                       | Order By Item IDs                                 | ``["d666a904-5739-46c0-b70a-1cd57658a3f6"]``          |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/engagement/service_points"
    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    # filter example: pagination
    #service_url += "?page=0&limit=100"

    # filter example: name
    #service_url += "?name=MyServicePointName"

    # filter example: type_id
    #service_url += "?type_id=d666a904-5739-46c0-b70a-1cd57658a3f6"

    # filter example: entity_id
    #service_url += "?entity_id=d666a904-5739-46c0-b70a-1cd57658a3f6"

    # filter example: postcode (dynamic field)
    #service_url += "?postcode=1234AB"

    # filter example: to use multiple filters, use the & character between the filters
    #service_url += "?name=MyServicePointName" + "&postcode=1234AB"

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
