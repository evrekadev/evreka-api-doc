.. raw:: pdf

   PageBreak

Delete Order API
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | DELETE               | ``/orders/{order_id}``                  |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
Order ID is required UUID for the order to be deleted.

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python


    import requests
    import json

    EVREKA360_BASE_URL = ""
    ACCESS_TOKEN = ""

    session = requests.session()

    order_id = ""
    service_url = "/engagement/orders/" + order_id
    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }
    
    response = session.delete(EVREKA360_BASE_URL + service_url, headers=headers)
    response_dict = json.loads(response._content.decode('utf-8'))
    print(response_dict) 


Response
^^^^^^^^^^^^^^^^^

*Status Code:* ``200`` - Retrieved successfully
*Content Type:* ``application/json``
*Body:*

.. code-block:: json 

    {
        "detail": "Successfully deleted Order ({order_name})"
    }

*Status Code:* ``404`` - Not Found
*Content Type:* ``application/json``
*Body:*

.. code-block:: json 

    {
        "detail": "Order ({order_id}) not found"
    }

