Generic MRF Dynamic Field List
--------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/{content_type}/dynamic_fields``         |
   +-------------------+--------------------------------------------+

Valid ``content_type`` values:

- ``parcels``
- ``consignments``
- ``inventory_items``
- ``inbounds``
- ``processes``
- ``materials``
- ``activities``


Data Structure
^^^^^^^^^^^^^^^^^
There is no required parameter for this request.

Example Code
^^^^^^^^^^^^^^^^^
.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    content_type = "inbounds"

    service_url = f"/{content_type}/dynamic_fields"
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
                "id": "Dynamic Field ID - UUID",
                "extra": "Extra - String",
                "external_id": "External ID - String",
                "key": "Key - String",
                "header": "Header - String",
                "required": "Is Required - Boolean",
                "type": "Type - Integer",
                "options": "Options - String",
                "default_value": "Default Value",
                "sequence": "Sequence - Integer",
            }
        ]
    }
