.. raw:: pdf

   PageBreak

Order Detail API
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/orders/{order_id}``                     |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
Order ID is required UUID for the order to retrieve details.

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    order_id = ""
    service_url = "/engagement/orders/" + order_id
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
        "id": "UUID",
        "name": "string",
        "created_at": "datetime - UTC",
        "updated_at": "datetime - UTC",
        "type": {
            "id": "UUID",
            "name": "string"
        },
        "status": {
            "id": "UUID",
            "name": "string"
        },
        "entity": {
            "id": "UUID",
            "name": "string",
            "type_id": "UUID"
        },
        "service_point": {
            "id": "UUID",
            "name": "string",
            "type_id": "UUID"
        },
        "fulfillment_date": "date",
        "price": {
            "value": "float",
            "currency": "string"
        },
        "planned_price": {
            "value": "float",
            "currency": "string"
        },
        "address": "string",
        "latitude": "float",
        "longitude": "float",
        "dynamic": {
            "key": "value",
        },
        "note": "string"
    }

*Status Code:* ``404`` - Not Found
*Content Type:* ``application/json``
*Body:*

.. code-block:: json 

    {
        "detail": "Order ({order_id}) not found"
    } 