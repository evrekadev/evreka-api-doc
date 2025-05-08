Entity List
----------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/entities``                              |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^

.. table::

   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
   +=========================+==============================================================+===================================================+=======================================================+
   | name                    | string *(optional)*                                          | Entity Name                                       | MyEntity                                              |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | type_id                 | string *(optional)*                                          | Entity Type ID - UUID                             | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
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

    service_url = "/engagement/entities"
    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }
    
    # filter example #1
    #service_url += "?page=1&limit=10"

    # filter example #2
    #service_url += "?name=MyEntity"

    # filter example #3
    #service_url += "?type_id=d666a904-5739-46c0-b70a-1cd57658a3f6"

    # filter example #4 
    #service_url += "?postcode=1234AB"

    # filter example #5 #To use multiple filters, use the & character between the filters.
    #service_url += "?name=MyServicePointName" + "&postcode=1234AB"

    # filter example #6 #To use exact or contains filters, use the __exact or __contains modifier. If not specified, the default is contains.
    #service_url += "?postcode__contains=1234AB"

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
                "name": "Entity Name",
                "type_id": "Entity Type UUID",
                "type_name": "Entity Type Name",
                "status_id": "Entity Status UUID",
                "dynamic": "Dynamic Field JSON"
            }
        ]
    }
