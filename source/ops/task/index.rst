Task API List
======================

.. toctree::
   :maxdepth: 2
   :caption: Task

   
   detail
   transitions
   step-detail
   list

This part provides documentation for available API endpoints of Task Model for OPS Module.


.. table::
   :width: 100%

   +-----------+-----------------------------------------------------+-------------------------------------------+
   | Method    | Endpoint                                            | Description                               |
   +===========+=====================================================+===========================================+
   | GET       | /tasks                                              | Retrieve list of the tasks                |
   +-----------+-----------------------------------------------------+-------------------------------------------+
   | GET       | /tasks/{task_id}                                    | Retrieve details of the task              |
   +-----------+-----------------------------------------------------+-------------------------------------------+
   | GET       | /tasks/{task_id}/transitions                        | Retrieve transitions of the task          |
   +-----------+-----------------------------------------------------+-------------------------------------------+
   | GET       | /tasks/{task_id}/transitions/{transition_id}/       | Retrieve details of the step with given   |
   |           | /steps/{step_id}                                    |                                           |
   +-----------+-----------------------------------------------------+-------------------------------------------+
