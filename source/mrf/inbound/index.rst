Inbound API List
======================

.. toctree::
   :maxdepth: 2
   :caption: Order

   status-list
   edit-inbound-attachments

This part provides documentation for available API endpoints of Inbound Model for MRF Module.


.. table::
   :width: 100%

   +-----------+-----------------------------------------+-------------------------------------------+
   | Method    | Endpoint                                | Description                               |
   +===========+=========================================+===========================================+
   | GET       | /inbounds/status                        | Retrive status list of inbound model      |
   +-----------+-----------------------------------------+-------------------------------------------+
   | POST      | /inbounds/{inbound_id}/edit_attachments | Update attachments of the given inbound   |
   +-----------+-----------------------------------------+-------------------------------------------+
