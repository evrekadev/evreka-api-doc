Service Point API List
======================

.. toctree::
   :maxdepth: 2
   :caption: Service Point

   list
   asset_types
   asset_list
   locations_list


This section provides documentation for available API endpoints of the Service Point Model for the Engagement Module.

.. table::

   +-----------+---------------------------------------------+-----------------------------------------------------------------------------+
   | Method    | Endpoint                                    | Description                                                                 |
   +===========+=============================================+=============================================================================+
   | GET       | /service_points                             | Retrieve list of service points with                                        |
   |           |                                             | optional parameters                                                         |
   +-----------+---------------------------------------------+-----------------------------------------------------------------------------+
   | GET       | /service_points/{service_point}/asset_types | Retrieve list of asset types of assets currently linked to a service point  |
   +-----------+---------------------------------------------+-----------------------------------------------------------------------------+
   | GET       | /service_points/{service_point}/assets      | Retrieve list of assets currently linked to a service point                 |
   +-----------+---------------------------------------------+-----------------------------------------------------------------------------+
   | GET       | /service_points_locations/                  | Retrieve list of locations of service points with optional parameters and   |
   |           |                                             | no pagination                                                               |
   +-----------+---------------------------------------------+-----------------------------------------------------------------------------+