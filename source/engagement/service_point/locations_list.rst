Service Points Locations API List
---------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/service_points_locations``              |
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
   | case_type_id            | string *(optional)*                                          | Case Type ID - UUID                               | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | bound_filter            | dict object *(optional)*                                     | Bound Filter Coordinates                          | {"north_east":{"lat":90,"lng":250},                   |
   |                         |                                                              |                                                   | "south_west":{"lat":-90,"lng":-250}}                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/engagement/service_points_locations"
    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    # filter example: name
    #service_url += "?name=MyServicePointName"

    # filter example: type_id
    #service_url += "?type_id=d666a904-5739-46c0-b70a-1cd57658a3f6"

    # filter example: entity_id
    #service_url += "?entity_id=d666a904-5739-46c0-b70a-1cd57658a3f6"

    # filter example: case_type_id
    #service_url += "?case_type_id=d666a904-5739-46c0-b70a-1cd57658a3f6"

    # filter example: bound_filter
    #service_url += "?bound_filter={\"north_east\":{\"lat\":90,\"lng\":250},\"south_west\":{\"lat\":-90,\"lng\":-250}}"
    
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
                "id": "Service Point ID - UUID",
                "name": "Service Point Name - String",
                "type_id": "Service Point Type - UUID",
                "type_name": "Service Point Type Name - String",
                "status_id": "Service Point Status ID - UUID",
                "address": "Service Point Address - String",
                "latitude": "Service Point Latitude - Float",
                "longitude": "Service Point Longitude - Float",
                "dynamic": "Dynamic Field JSON"
            }
        ]
    }

*Status Code:* ``404`` - Not Found
*Content Type:* ``application/json``
*Body:*

.. code-block:: json

    {
        "message": "Service Point Not Found"
    }
