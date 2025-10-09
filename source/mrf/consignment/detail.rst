.. raw:: pdf

   PageBreak

Consignment Detail API
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/consignments/{consignment_id}``         |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
``consignment_id`` must be provided to retrieve the consignment details.

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests
    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""
    #Data Example 1
    consignment_id = "5546"
    service_url = "/mrf/consignments" + f"/{consignment_id}"
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
        "id": "Consignment ID - Integer",
        "external_id": "External ID - String",
        "name": "Consignment Name - String",
        "created_at": "Creation Date - String",
        "updated_at": "Update Date - String",
        "due_date": "Due Date - String",
        "status": {
            "id": "Status ID - Integer",
            "step": "Status Step - Integer",
            "name": "Status Name - String",
            "color": "Status Color - String"
        },
        "consignment_type": {
            "id": "Consignment Type ID - Integer",
            "name": "Consignment Type Name - String"
        },
        "entity": {
            "id": "Entity ID - UUID",
            "name": "Entity Name - String"
        },
        "branch": {
            "id": "Branch ID - Integer",
            "name": "Branch Name - String"
        },
        "linked_order": {
            "id": "Linked Order ID - UUID",
            "name": "Linked Order Name - String"
        },
        "transfer_client": {
            "id": "Transfer Client ID - Integer",
            "name": "Transfer Client Name - String"
        },
        "materials": [
            {
                "id": "Material ID - Integer",
                "planned_amount": "Planned Amount - Float",
                "actual_amount": "Actual Amount - Float",
                "planned_weight": "Planned Weight - Float",
                "gross_weight": "Gross Weight - Float",
                "tare_weight": "Tare Weight - Float",
                "net_weight": "Net Weight - Float",
                "weight_uom": "Weight UOM - String",
                "quantity_uom": "Quantity UOM - String",
                "ewc_code": {
                    "value": "EWC Code Value - String",
                    "label": "EWC Code Label - String",
                    "hazardous": "Is Hazardous - Boolean",
                    "description": "EWC Code Description - String"
                },
                "dynamic": "Dynamic Field JSON",
                "weight_source": "Weight Source - String",
                "edit_weight_note": "Edit Weight Note - String",
                "planned_volume": "Planned Volume - Float", // If client has calculate_density_enabled
                "net_volume": "Net Volume - Float", // If client has calculate_density_enabled feature
                "volume_uom": "Volume UOM - String" // If client has calculate_density_enabled feature
            }
        ],
        "media": [
            {
                "id": "Media ID - Integer",
                "media_name": "Media Name - String",
                "media_url": "Media URL - String"
            }
        ],
        "dynamic": "Dynamic Field JSON"
    }


*Status Code:* ``404`` - Not Found
*Content Type:* ``application/json``
*Body:*

.. code-block:: json 

    {
        "detail": "Consignment not found"
    }