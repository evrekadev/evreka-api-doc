Case API List
======================

.. toctree::
   :maxdepth: 2
   :caption: Case

   create
   case-list
   case-type-list
   case-status-list
   edit-case-attachments
   case-detail
   case-rate


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
   | GET       | /cases/case_types                   | Retrieve case type list of case model     |
   +-----------+-------------------------------------+-------------------------------------------+
   | GET       | /cases/status                       | Retrieve case status list of case model   |
   +-----------+-------------------------------------+-------------------------------------------+
   | POST      | /cases/{case_id}/edit_attachments   | Update attachments of the given case      |
   +-----------+-------------------------------------+-------------------------------------------+
   | GET       | /cases/{case_id}                    | Retrieve case                             |
   +-----------+-------------------------------------+-------------------------------------------+
   | POST      | /cases/{case_id}/rate               | Rate the given case                       |
   +-----------+-------------------------------------+-------------------------------------------+