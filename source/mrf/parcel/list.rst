Parcel List
------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/parcels``                               |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^


.. table::
    :width: 100%

    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
    +=========================+==============================================================+===================================================+=======================================================+
    | order_id                | UUID *(optional)*                                            | Id of related Order                               | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | inbound_id              | Integer *(optional)*                                         | Id of related Inbound                             | 123                                                   |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | task_id                 | Integer *(optional)*                                         | Id of related Task                                | 456                                                   |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    page = 1
    limit = 10
    order_id = "ORDER_ID_UUID"
    inbound_id = 123
    task_id = 456
    service_url = "/mrf/parcels"

    # filter example #1: default filter
    #service_url = "service_url"

    # filter example #2: filter with order_id
    #service_url += "?order_id=d666a904-5739-46c0-b70a-1cd57658a3f6"

    # filter example #3: filter with inbound_id and task_id
    #service_url += f"?inbound_id={inbound_id}&task_id={task_id_id}"

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
                "id": "Parcel ID - Integer",
                "name": "Parcel Name - String",
                "type": "Parcel Type - String",
                "arrive": "Arrival Timestamp - Nullable String (ISO 8601)",
                "carrier_type": "Carrier Type - Nullable String",
                "carrier": "Carrier Name - Nullable String",
                "gross_weight": "Gross Weight - Float (kg)",
                "net_weight": "Net Weight - Float (kg)",
                "tare_weight": "Tare Weight - Float (kg)",
                "weight_source": "Weight Source - String (Manual or Weighing Scale)",
                "edit_weight_note": "Edit Weight Note - Nullable String",
                "status": {
                    "id": "Status ID - Integer",
                    "name": "Status Name - String"
                },
                "operator": "Operator Name or ID - Nullable",
                "material": {
                    "id": "Material ID - Integer",
                    "name": "Material Name - String",
                },
                "parent": "Parent Parcel ID - Nullable Integer",
                "consignment": "Consignment ID - Nullable Integer",
                "create": "Created At - String (ISO 8601)",
                "update": "Updated At - String (ISO 8601)",
                "dynamic": "Dynamic Fields - Dictionary (Key-Value)"
            }
        ]
    }

*Status Code:* ``404`` - Not Found
*Content Type:* ``application/json``
*Body:*

.. code-block:: json

    {
        "detail": "Parcel not found"
    }