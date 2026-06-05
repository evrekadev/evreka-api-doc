Service Point API List
======================

.. toctree::
   :maxdepth: 2
   :caption: Service Point

   list
   change_default_items

This part provides documentation for available API endpoints of the Service Point Model for the OPS Module.

.. table::
   :width: 100%

   +-----------+--------------------------------------------------------+----------------------------------------------------------+
   | Method    | Endpoint                                               | Description                                              |
   +===========+========================================================+==========================================================+
   | GET       | /service_points                                        | List the service points of the authenticated client      |
   +-----------+--------------------------------------------------------+----------------------------------------------------------+
   | POST      | /service_points/{service_point_id}/default_items       | Add / remove / overwrite default Task Items on a single  |
   |           |                                                        | Service Point                                            |
   +-----------+--------------------------------------------------------+----------------------------------------------------------+
