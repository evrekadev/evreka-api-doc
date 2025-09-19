.. raw:: pdf

   PageBreak

Consignment API List
======================

.. toctree::
   :maxdepth: 2
   :caption: Order

   list
   status-list
   detail

This part provides documentation for available API endpoints of Consignment Model for MRF Module.


.. table::
   :width: 100%

   +-----------+-----------------------------------------+-------------------------------------------------------+
   | Method    | Endpoint                                | Description                                           |
   +===========+=========================================+=======================================================+
   | GET       | /consignments                           | Retrieve consignment list                             |
   +-----------+-----------------------------------------+-------------------------------------------------------+
   | GET       | /consignments/status                    | Retrieve consignment status list                      |
   +-----------+-----------------------------------------+-------------------------------------------------------+
   | GET       | /consignments/{consignment_id}          | Retrieve consignment detail with given consignment id |
   +-----------+-----------------------------------------+-------------------------------------------------------+