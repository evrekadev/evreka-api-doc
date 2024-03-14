Order Status List
---------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/orders/status``                         |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
There is no required parameter for this request.

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

   service_url = f"/engagement/orders/status"
   headers = {"Content-Type": "application/json; charset=utf-8"}
   resp = session.get(EVREKA360_BASE_URL + service_url, headers=headers)

Response
^^^^^^^^^^^^^^^^^
*Status Code:* ``200`` - Retrieved successfully
*Content Type:* ``application/json``
*Body:*

.. code-block:: json

    {
        "items": [
            {
                "id": "Status ID - UUID",
                "name": "Status Name"
            }
        ]
    }
