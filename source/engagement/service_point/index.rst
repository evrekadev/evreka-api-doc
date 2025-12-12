Service Point API List
======================

.. toctree::
   :maxdepth: 2
   :caption: Service Point

   create
   list
   detail
   types
   status-list
   dynamic_field_list
   nearest
   asset_types
   asset_list
   locations_list
   delete
   update

This section provides documentation for available API endpoints of the Service Point Model for the Engagement Module.

.. table::

   +-----------+------------------------------------------------+-----------------------------------------------------------------------------+
   | Method    | Endpoint                                       | Description                                                                 |
   +===========+================================================+=============================================================================+
   | POST      | /service_points                                | Create a service point with given parameters                                |
   +-----------+------------------------------------------------+-----------------------------------------------------------------------------+
   | GET       | /service_points                                | Retrieve list of service points with optional parameters                    |
   +-----------+------------------------------------------------+-----------------------------------------------------------------------------+
   | GET       | /service_points/{service_point_id}             | Retrieve details of a service point by its UUID                             |
   +-----------+------------------------------------------------+-----------------------------------------------------------------------------+
   | GET       | /service_points/types                          | Retrieve list of service point types with                                   |
   +-----------+------------------------------------------------+-----------------------------------------------------------------------------+
   | GET       | /service_points/status                         | Retrieve list of service point statuses                                     |
   +-----------+------------------------------------------------+-----------------------------------------------------------------------------+
   | GET       | /service_points/dynamic_fields                 | Retrieve dynamic fields of service points with                              |
   |           |                                                | optional parameters                                                         |
   +-----------+------------------------------------------------+-----------------------------------------------------------------------------+
   | GET       | /service_points/nearest                        | Retrieve list of service points that ordered by distance to given location  |
   +-----------+------------------------------------------------+-----------------------------------------------------------------------------+
   | GET       | /service_points/{service_point_id}/asset_types | Retrieve list of asset types of assets currently linked to a service point  |
   +-----------+------------------------------------------------+-----------------------------------------------------------------------------+
   | GET       | /service_points/{service_point_id}/assets      | Retrieve list of assets currently linked to a service point                 |
   +-----------+------------------------------------------------+-----------------------------------------------------------------------------+
   | GET       | /service_points_locations/                     | Retrieve list of locations of service points with optional parameters and   |
   |           |                                                | no pagination                                                               |
   +-----------+------------------------------------------------+-----------------------------------------------------------------------------+
   | DELETE    | /service_points/{service_point_id}             | Delete the given service point                                              |
   +-----------+------------------------------------------------+-----------------------------------------------------------------------------+
   | POST      | /service_points/{service_point_id}             | Update the given service point with new parameters                          |
   +-----------+------------------------------------------------+-----------------------------------------------------------------------------+