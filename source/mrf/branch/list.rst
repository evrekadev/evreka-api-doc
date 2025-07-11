.. raw:: pdf

   PageBreak

Branch List API
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/branches``                              |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^

If ``parent_id`` is provided as 0, branches without a parent branch will be listed.

.. table::

   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
   +=========================+==============================================================+===================================================+=======================================================+
   | parent_id               | integer *(optional)*                                         | Parent Branch ID - Integer                        | 4                                                     |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | order_by                | string *(optional)*                                          | Order by asc/desc on name, asc by default         | asc                                                   |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+


Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/mrf/inbounds"
    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    # pagination example
    #service_url += "?page=1&limit=10"

    # filter example #1
    #service_url += "?parent_id=0"

    # filter example #2
    #service_url += "?order_by=desc"

    # filter example #3
    #service_url += "?parent_id=4" + "&order_by=desc"

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
                "id": "Branch ID - Integer",
                "name": "Branch Name - String",
                "parent_id": "Parent Branch ID - Integer (null if no parent branch)"
            }
        ]
    }

*Status Code:* ``404`` - Not Found

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

    {
        "detail": "Branch not found"
    }

