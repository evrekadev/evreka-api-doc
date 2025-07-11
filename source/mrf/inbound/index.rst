Inbound API List
======================

.. toctree::
   :maxdepth: 2
   :caption: Order

   create
   list
   detail
   status-list

This part provides documentation for available API endpoints of Inbound Model for MRF Module.


.. table::
   :width: 100%

   +-----------+-------------------------------------+-----------------------------------------------+
   | Method    | Endpoint                            | Description                                   |
   +===========+=====================================+===============================================+
   | POST      | /inbounds                           | Create an inbound with given parameters       |
   +-----------+-------------------------------------+-----------------------------------------------+
   | GET       | /inbounds                           | Retrieve inbound list                         |
   +-----------+-------------------------------------+-----------------------------------------------+
   | GET       | /inbounds/{inbound_id}              | Retrieve inbound detail with given inbound id |
   +-----------+-------------------------------------+-----------------------------------------------+
   | GET       | /inbounds/status                    | Retrive status list of inbound model          |
   +-----------+-------------------------------------+-----------------------------------------------+
   
