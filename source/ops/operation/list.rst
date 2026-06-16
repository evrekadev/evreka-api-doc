Operation List
------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/operations``                            |
   +-------------------+--------------------------------------------+

Returns the operations that belong to the authenticated client. Results are
ordered by ``id`` descending and are paginated.

Data Structure
^^^^^^^^^^^^^^^^^


.. table::
    :width: 100%

    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
    +=========================+==============================================================+===================================================+=======================================================+
    | name                    | String *(optional)*                                          | Case-insensitive filter on the operation name     | Collection                                            |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | page                    | Integer *(optional)*                                         | Page number (default 1)                           | 1                                                     |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | limit                   | Integer *(optional)*                                         | Items per page (default 10, max 50)               | 10                                                    |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    page = 1
    limit = 10
    name = "Collection"
    service_url = f"/ops/operations"

    # filter example #1: default filter
    #service_url = "service_url"

    # filter example #2: filter with name
    #service_url += f"?name={name}"

    # filter example #3: filter with name and pagination
    #service_url += f"?name={name}&page={page}&limit={limit}"


    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

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
                "id": "Operation ID - Integer",
                "name": "Operation Name - String",
                "assignee_type": "Assignee Type - String (\"vehicle\" or \"employee\")"
            }
        ]
    }

*Status Code:* ``404`` - Not Found
*Content Type:* ``application/json``
*Body:*

.. code-block:: json

    {
        "detail": "Operation not found"
    }
