.. raw:: pdf

   PageBreak

Consignment List API
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/consignments``                          |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
.. table::

   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
   +=========================+==============================================================+===================================================+=======================================================+
   | status_id               | integer *(optional)*                                         | Status ID - Integer                               | 1                                                     |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | type_id                 | integer *(optional)*                                         | Type ID - Integer                                 | 1                                                     |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | due_date_from           | string *(optional)*                                          | Start Date of Due Date Range                      | 2025-01-01                                            |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | due_date_to             | string *(optional)*                                          | End Date of Due Date Range                        | 2025-01-01                                            |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | updated_from            | string *(optional)*                                          | Start Date of Updated Date Range                  | 2025-01-01                                            |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | updated_to              | string *(optional)*                                          | End Date of Updated Date Range                    | 2025-01-01                                            |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | dynamic_field_key       | string *(optional)*                                          | Dynamic Field Key                                 | offload_id                                            |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | dynamic_field_value     | string *(optional)*                                          | Dynamic Field Value                               | OffloadID                                             |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
  

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/mrf/consignments"
    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    # pagination example
    #service_url += "?page=1&limit=10"

    # filter example #1
    #service_url += "?status_id=1"

    # filter example #2
    #service_url += "?type_id=1"

    # filter example #3
    #service_url += "?due_date_from=2025-01-01"

    # filter example #4
    #service_url += "?due_date_to=2025-01-01"

    # filter example #5
    #service_url += "?updated_from=2025-01-01"

    # filter example #6
    #service_url += "?updated_to=2025-01-01"

    # filter example #7
    #service_url += "?dynamic_field_key=offload_id&dynamic_field_value=OffloadID"

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
                "id": "Consignment ID - Integer",
                "name": "Consignment Name - String",
                "status_id": "Status ID - Integer",
                "type_id": "Type ID - Integer",
                "due_date": "Due Date - String",
                "created_at": "Created At - ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>",
                "updated_at": "Updated At - ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>",
                "dynamic": {
                    "offload_id": "Offload ID - String"
                }
            }
        ]
    }

*Status Code:* ``404`` - Not Found

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

    {
        "detail": "Consignment not found"
    }

