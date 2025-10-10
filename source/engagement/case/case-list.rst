Case List
----------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/cases``                                 |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^

.. table::

   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
   +=========================+==============================================================+===================================================+=======================================================+
   | contact_id              | string *(optional)*                                          | Contact ID - UUID                                 | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | entity_id               | string *(optional)*                                          | Case Related Entity ID - UUID                     | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | case_type_id            | string *(optional)*                                          | Case Type ID - UUID                               | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | service_point_id        | string *(optional)*                                          | Service Point ID - UUID                           | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | order_by                | string *(optional)*                                          | Order by asc/desc on created_at, desc by default  | asc                                                   |
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

    # filter example #1: contact_id
    #service_url += "?contact_id=d666a904-5739-46c0-b70a-1cd57658a3f6"

    # filter example #2: entity_id
    #service_url += "?entity_id=d666a904-5739-46c0-b70a-1cd57658a3f6"

    # filter example #3: case_type_id
    #service_url += "?case_type_id=d666a904-5739-46c0-b70a-1cd57658a3f6"

    # filter example #4: service_point_id
    #service_url += "?service_point_id=d666a904-5739-46c0-b70a-1cd57658a3f6"

    # filter example #5: order_by (asc/desc)
    #service_url += "?order_by=asc"
    
    # filter example #5: to use multiple filters, use the & character between the filters.
    #service_url += "?case_type_id=d666a904-5739-46c0-b70a-1cd57658a3f6" + "&entity_id=d666a904-5739-46c0-b70a-1cd57658a3f6"

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
                "id": "Case ID - UUID",
                "name": "Case Name - String",
                "subject": "Case Subject - String",
                "entity": {
                    "id": "Entity ID - UUID",
                    "name": "Entity Name - String"
                },
                "status": {
                    "id": "Status ID - UUID",
                    "name": "Status Name - String",
                    "color": "Status Color - String"
                },
                "description": "Case Description - String",
                "service_point": {
                    "id": "Service Point ID - UUID",
                    "name": "Service Point Name - String"
                },
                "type": {
                    "id": "Case Type ID - UUID",
                    "name": "Case Type Name - String"
                },
                "sub_type": {
                    "id": "Case Sub Type ID - UUID",
                    "name": "Case Sub Type Name - String"
                },
                "contact": {
                    "id": "Contact ID - UUID",
                    "name": "Contact Full Name - String"
                },
                "assignee":  {
                    "id": "Assignee ID - Int",
                    "name": "Assignee Full Name - String"
                },
                "created_at": "Created At - UTC",
                "updated_at": "Updated At - UTC",
                "completed_time": "Completed Time - UTC",
                "latitude": "Latitude - Float",
                "longitude": "Longitude - Float",
                "rate": "Rate - Int",
                "rate_note": "Rate Note - String",
                "rate_viewed_time": "Rate Viewed Time - ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>"
            }
        ]
    }