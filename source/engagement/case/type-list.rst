Case Type List
----------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/cases/case_types``                      |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^

.. table::

   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
   +=========================+==============================================================+===================================================+=======================================================+
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/engagement/cases"
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
                "name": "Case Name",
                "location_type": "Case Location Type",
                "sub_type_list": "Case Sub Type List",
                "service_point_types": "Case Service Point Type List",
                "must_have_sub_type": "true/false",
                "is_entity_related": "true/false",
                "is_citizen_related": "true/false",
        ]
    }
