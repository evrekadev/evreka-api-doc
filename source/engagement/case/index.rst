Case API List
======================

.. toctree::
   :maxdepth: 2
   :caption: Case

   create
   case-type-list
   case-list
   edit-case-attachments
   case-detail
   

This part provides documentation for available API endpoints of Case Model for Engagement Module.


.. table::
   :width: 100%

   +-----------+-------------------------------------+-------------------------------------------+
   | Method    | Endpoint                            | Description                               |
   +===========+=====================================+===========================================+
   | POST      | /cases                              | Create a case with given parameters       |
   +-----------+-------------------------------------+-------------------------------------------+
   | GET       | /cases                              | Retrieve cases with optional filters      |
   +-----------+-------------------------------------+-------------------------------------------+
   | GET       | /cases/case_types                   | Retrieve case type list of contact model  |
   +-----------+-------------------------------------+-------------------------------------------+
   | POST      | /cases/{case_id}/edit_attachments   | Update attachments of the given case      |
   +-----------+-------------------------------------+-------------------------------------------+
   | GET       | /cases/{case_id}                    | Retrieve case                             |
   +-----------+-------------------------------------+-------------------------------------------+
