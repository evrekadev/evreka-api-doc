.. raw:: pdf

   PageBreak

Consignment API List
======================

.. toctree::
   :maxdepth: 2
   :caption: Order

   list
   status-list
   types-list
   change-status
   create
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
   | GET       | /consignments/types                     | Retrieve consignment types list                       |
   +-----------+-----------------------------------------+-------------------------------------------------------+
   | POST      | /consignments/{consignment_id}/status   | Update consignment status                             |
   +-----------+-----------------------------------------+-------------------------------------------------------+
   | POST      | /consignments                           | Create consignment                                    |
   +-----------+-----------------------------------------+-------------------------------------------------------+
   | GET       | /consignments/{consignment_id}          | Retrieve consignment detail                           |
   +-----------+-----------------------------------------+-------------------------------------------------------+