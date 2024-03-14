Delete Order API
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | DELETE               | ``/orders/{order_id}``                  |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
Order ID is required UUID for the order to be deleted.
One of the following fields must be provided: service_point_id, latitude and longitude. If both are provided, service_point_id will be used.
If any required dynamic field exists for the order type, it must be provided in the request.


Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    service_url = f"/engagement/orders/{order_id}
    headers = {"Content-Type": "application/json; charset=utf-8"}
    resp = session.delete(EVREKA360_BASE_URL + service_url, headers=headers)


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
        "detail": "Order (33fcec27-3933-418e-b2b5-4d3ee1cff4e6) not found"
    }

