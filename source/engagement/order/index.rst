Order API List
======================

.. toctree::
   :maxdepth: 2
   :caption: Order

   create
   delete
   update-status
   status-list
   dynamic-list

This part provides documentation for available API endpoints of Order Model for Engagement Module.


.. table::
   :width: 100%

   +-----------+-------------------------------------+-------------------------------------------+
   | Method    | Endpoint                            | Description                               |
   +===========+=====================================+===========================================+
   | POST      | /orders                             | Create an order with given parameters     |
   +-----------+-------------------------------------+-------------------------------------------+
   | DELETE    | /orders/{order_id}                  | Delete the order with given order id      |
   +-----------+-------------------------------------+-------------------------------------------+
   | PUT       | /orders/{order_id}/status           | Update status of order with given order id|
   +-----------+-------------------------------------+-------------------------------------------+
   | GET       | /orders/dynamic_fields              | Retrive dynamic fields of order model     |
   +-----------+-------------------------------------+-------------------------------------------+
   | GET       | /orders/status                      | Retrive status list of order model        |
   +-----------+-------------------------------------+-------------------------------------------+
