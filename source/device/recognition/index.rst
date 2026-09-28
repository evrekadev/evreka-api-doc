Recognition API List
======================

.. toctree::
   :maxdepth: 2
   :caption: Recognition

   create

This part provides documentation for available API endpoints of Recognition Model for Device Module.

Recognition endpoint classifies the object in a given image with the AI model and returns the detected waste type with a confidence score. Objects that do not match an accepted waste type are rejected.


.. table::
   :width: 100%

   +--------+---------------------+-----------------------------------------+
   | Method | Endpoint            | Description                             |
   +========+=====================+=========================================+
   | POST   | /device/recognition | Recognize the object in the given image |
   +--------+---------------------+-----------------------------------------+
