.. raw:: pdf

   PageBreak

Order List API
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/orders``                                |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
.. table::

   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
   +=========================+==============================================================+===================================================+=======================================================+
   | name                    | string *(optional)*                                          | Order Name                                        | MyOrder                                               |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | type_id                 | string *(optional)*                                          | Order Type ID - UUID                              | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | entity_id               | string *(optional)*                                          | Order Entity ID - UUID                            | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | service_point_id        | string *(optional)*                                          | Order Service Point ID - UUID                     | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | order_plan_id           | string *(optional)*                                          | Order Order Plan ID - UUID                        | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | contact_id              | string *(optional)*                                          | Order Contact ID - UUID                           | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
  

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/engagement/orders"
    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    # pagination example
    #service_url += "?page=1&limit=10"

    # filter example #1
    #service_url += "?name=MyOrder"

    # filter example #2
    #service_url += "?type_id=d666a904-5739-46c0-b70a-1cd57658a3f6"

    # filter example #3 
    #service_url += "?my_dynamic_field=1234AB"

    # filter example #4 
    # To use multiple filters, use the & character between the filters.
    #service_url += "?name=MyOrder" + "&my_dynamic_field=1234AB"

    # filter example #5 #To use exact or contains filters, use the __exact or __contains modifier. If not specified, the default is contains.
    #service_url += "?my_dynamic_field__contains=1234AB"
    
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
                "name": "string",
                "created_at": "datetime - ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>",
                "updated_at": "datetime - ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>",
                "type_id": "UUID",
                "status_id": "UUID",
                "entity_id": "UUID",
                "service_point_id": "UUID",
                "fulfillment_date": "date - YYYY-MM-DD",
                "address": "string",
                "latitude": "float",
                "longitude": "float",
                "dynamic": {
                    "key": "value"
                },
                "note": "string"
                "completion_time": "optional datetime - ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>"
            }
        ]
    }
