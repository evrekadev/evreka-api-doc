.. raw:: pdf

   PageBreak

Update Order Status API
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | PUT               | ``/orders/{order_id}/status``              |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
New status ID must be provided in the request body.

.. table::
    :width: 100%

    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
    +=========================+==============================================================+===================================================+=======================================================+
    | status_id               | string *(required)*                                          | Status ID - UUID                                  | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+


Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_BASE_URL = ""
    ACCESS_TOKEN = ""

    session = requests.session()

    order_id = ""

    service_url = "/engagement/orders/" + order_id + "/status"
    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    data = {
        "status_id": ""
    }

    resp = session.put(EVREKA360_BASE_URL + service_url, json=data, headers=headers)
    print(resp.status_code, resp.json())

Response
^^^^^^^^^^^^^^^^^
*Status Code:* ``200`` - Retrieved successfully
*Content Type:* ``application/json``
*Body:*

.. code-block:: json 

    {
        "detail": "Order status updated successfully"
    }


*Status Code:* ``400`` - Bad request
*Content Type:* ``application/json``
*Body:*

.. code-block:: json 

    {
        "detail": "Order ({order_id}) not found"
    }

