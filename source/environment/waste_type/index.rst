Waste Type List
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET              | ``/environment/waste_types``                |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^

.. table::
    :width: 100%

    +---------------------+--------------------------+-------------------------------------------------+
    | Field Name          | Data type                | Description                                     |
    +=====================+==========================+=================================================+
    | name_contains       | string *(optional)*      | Name of the waste type                          |
    +---------------------+--------------------------+-------------------------------------------------+
   
Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/environment/waste_types"
    headers = {
        "Content-Type": "Content-Type: application/json",
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    # filter example
    # service_url += "?name_contains=plastic"

    resp = requests.get(EVREKA360_API_BASE_URL + service_url, headers=headers)
    print(resp.status_code, resp.json())

Response
^^^^^^^^^^^^^^^^^
*Status Code:* ``200`` - Retrieved successfully

*Content Type:* ``application/json``

*Body:*

.. code-block:: json 

    {
        "items": 
        [
            {
                "waste_type_id": 1,
                "waste_type_name": "Plastic",
            }
        ]
    }
