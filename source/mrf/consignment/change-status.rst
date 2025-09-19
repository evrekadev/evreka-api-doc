.. raw:: pdf

   PageBreak

Update Consignment Status API
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | POST              | ``/consignments/{consignment}/status``     |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
New status ID must be provided in the request body.

.. table::
    :width: 100%

    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
    +=========================+==============================================================+===================================================+=======================================================+
    | status                  | integer *(required)*                                         | Step of the status                                | 1                                                     |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+


Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    session = requests.session()

    consignment_id = ""

    service_url = "/mrf/consignments/" + consignment_id + "/status"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    data = {
        "status": ""
    }

    resp = session.post(EVREKA360_API_BASE_URL + service_url, json=data, headers=headers)
    print(resp.status_code, resp.json())

Response
^^^^^^^^^^^^^^^^^
*Status Code:* ``200`` - Retrieved successfully
*Content Type:* ``application/json``
*Body:*

.. code-block:: json

    {
        "detail": "Consignment status updated successfully"
    }


*Status Code:* ``400`` - Bad request
*Content Type:* ``application/json``
*Body:*

.. code-block:: json

    {
        "detail": "Consignment ({consignment_id}) not found"
    }

