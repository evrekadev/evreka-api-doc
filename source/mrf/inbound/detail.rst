.. raw:: pdf

   PageBreak

Inbound Detail API
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/inbounds/{inbound_id}``                 |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
``inbound_id`` must be provided to retrieve the inbound details.

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    #Data Example 1
    inbound_id = "67890"
    service_url = "/mrf/inbounds" + f"/{inbound_id}"

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

{
    "id": 69203,
    "external_id": "feyza test inb2",
    "name": "feyza test inb2",
    "created_at": "2025-07-03T12:06:09+00:00",
    "updated_at": "2025-07-03T12:06:09+00:00",
    "arrive": "2025-07-10",
    "status": {
        "id": 6,
        "name": "New",
        "color": "primary"
    },
    "assigned_to": null,
    "entity": null,
    "branch": {
        "id": 23,
        "name": "Yeniköy Fabrikası > Boyahane > Boya Kabinleri"
    },
    "linked_order": null,
    "materials": [
        {
            "id": 24207,
            "actual_quantity": 2,
            "planned_quantity": 1,
            "planned_weight": 23.0,
            "gross_weight": 25.0,
            "tare_weight": 2.0,
            "net_weight": 18.0,
            "weight_uom": 0,
            "quantity_uom": 7,
            "outages": [
                {
                    "id": 1,
                    "type": 0,
                    "amount": 5.0
                }
            ],
            "ewc_code": {
                "value": "CODE_00_00_00",
                "label": "00 00 00",
                "hazardous": false,
                "description": "The waste is not specified in the EWC list"
            },
            "dynamic": {},
            "weight_source": "manual",
            "edit_weight_note": null,
            "planned_volume": null,
            "net_volume": null,
            "volume_uom": "m³"
        }
    ],
    "attachments": [],
    "dynamic": {
        "dyndyn": 1,
        "test_key": "---",
        "text-area": "default text area"
    }
}

.. code-block:: json 

    {
        "id": "Inbound ID - Integer",
        "external_id": "External ID - String",
        "name": "Inbound Name - String",
        "created_at": "Creation Date - String",
        "updated_at": "Update Date - String",
        "arrive": "Arrival Date - String",
        "status": {
            "id": "Status ID - Integer",
            "name": "Status Name - String",
            "color": "Status Color - String"
        },
        "assigned_to": {
            "id": "Assigned Parcel ID - Integer",
            "name" : "Assigned Parcel Name - String"
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
        "materials": [
            {
                "id": "Material ID - Integer",
                "actual_quantity": "Actual Quantity - Float",
                "planned_quantity": "Planned Quantity - Float",
                "planned_weight": "Planned Weight - Float",
                "gross_weight": "Gross Weight - Float",
                "tare_weight": "Tare Weight - Float",
                "net_weight": "Net Weight - Float",
                "weight_uom": "Weight UOM - String",
                "quantity_uom": "Quantity UOM - String",
                "outages": [
                    {
                        "id": "Outage ID - Integer",
                        "type": "Outage Type - Integer",
                        "amount": "Outage Amount - Float"
                    }
                ],
                "ewc_code": {
                    "value": "EWC Code Value - String",
                    "label": "EWC Code Label - String",
                    "hazardous": "Is Hazardous - Boolean",
                    "description": "EWC Code Description - String"
                },
                "dynamic": "Dynamic Field JSON"
                "weight_source": "Weight Source - String",
                "edit_weight_note": "Edit Weight Note - String",
                "planned_volume": "Planned Volume - Float",
                "net_volume": "Net Volume - Float",
                "volume_uom": "Volume UOM - String"
            }
        ],
        "attachments": {
            "id": "Attachment ID - Integer",
            "media_name": "Attachment Media Name - String",
            "media_url": "Attachment Media URL - String",
        },
        "dynamic": "Dynamic Field JSON"
    }

*Status Code:* ``404`` - Not Found
*Content Type:* ``application/json``
*Body:*

.. code-block:: json 

    {
        "detail": "Inbound not found"
    }
