.. raw:: pdf

   PageBreak

Material List API
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/materials``                             |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
There is no required parameter for this request.

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/mrf/materials"
    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    # pagination example
    #service_url += "?page=1&limit=10"

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
                "id": "Material ID - Integer",
                "created_at": "Created At - ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>",
                "updated_at": "Updated At - ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>",
                "ewc_code": {
                    "value": "EWC Code Value - String",
                    "label": "EWC Code Label - String",
                    "hazardous": "Is Hazardous - Boolean",
                    "description": "EWC Code Description - String"
                },
                "name": "Material Name - String",
                "parent_materials": [
                    {
                        "id": "Parent Material ID - Integer",
                        "name": "Parent Material Name - String"
                    }
                ],
                "weight_uom": "Weight UOM - String",
                "quantity_uom": "Quantity UOM - String",
                "capacity_min_limit": {
                    "value": "Minimum Capacity Value - Float",
                    "uom": "Minimum Capacity UOM - String"
                },
                "capacity_max_limit": {
                    "value": "Maximum Capacity Value - Float",
                    "uom": "Maximum Capacity UOM - String"
                },
                "density": {
                    "value": "Density Value - Float",
                    "uom": "Density UOM - String"
                },
                "branches": [
                    {
                        "id": "Branch ID - Integer",
                        "name": "Branch Name - String"
                    }
                ],
                "unit_price_value": {
                    "value": "Unit Price Value - Float",
                    "currency": "Currency - String",
                    "unit": "Unit - String"
                },
                "dynamic": "Dynamic Field JSON"

            }
        ]
    }

*Status Code:* ``404`` - Not Found

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

    {
        "detail": "Material not found"
    }

