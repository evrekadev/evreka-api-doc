Entity List
----------------

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

    import requests
    import json

    EVREKA360_BASE_URL = ""
    ACCESS_TOKEN = ""

    session = requests.session()

    service_url = "/engagement/service_points"
    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    # filter example #1
    #service_url += "?page=0&limit=100"

    # filter example #2
    #service_url += "?name=MyServicePointName"

    # filter example #3
    #service_url += "?type=d666a904-5739-46c0-b70a-1cd57658a3f6"

    # filter example #4 
    #service_url += "?postcode=1234AB"

    # filter example #5 #To use multiple filters, use the & character between the filters.
    #service_url += "?name=MyServicePointName" + "&postcode=1234AB"

    response = session.get(EVREKA360_BASE_URL + service_url, headers=headers)
    response_dict = json.loads(response._content.decode('utf-8'))
    print(response_dict)  

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
