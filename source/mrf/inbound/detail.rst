.. raw:: pdf

   PageBreak

Inbound Detail API
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/inbounds``                              |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
Either ``inbound_id`` or ``external_id`` must be provided as a query parameter to retrieve the inbound details. If both are provided, ``inbound_id`` will be used.

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    #Data Example 1
    inbound_id = "67890"
    service_url = "/mrf/inbounds" + f"?inbound_id={inbound_id}"

    #Data Example 2
    # external_id = "external-12345"
    # service_url = "/mrf/inbounds" + f"?external_id={external_id}"

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
                "weight_uom": "Weight UOM ID - Integer",
                "quantity_uom": "Quantity UOM ID - Integer",
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
