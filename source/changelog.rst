Changelog
=================

1.3.2
----------------
- **entity_id** filter was added to :doc:`Engagement ServicePoint <engagement/service_point/list>`.

1.4.0
----------------
- Added new endpoint to create gps data of device by location :doc:`Fleet Service <fleet/index>`.

1.4.1
----------------
- Added new endpoint to create weight activity :doc:`Device Service <device/index>`.

1.4.2
----------------
- The optional type_id was changed to type_ids, and it will now return a UUID array. :doc:`Engagement Order Dynamic Fields <engagement/order/dynamic-list>`.
- It now also returns the template ID of the order types. :doc:`Engagement Order Settings <engagement/order_settings/get>`.

1.5.0
----------------
- Added new endpoint to get all waste types :doc:`Environment Service <environment/index>`.
- Added new waste_type_id field to weight activity :doc:`Device Service <device/index>`.

1.6.0
----------------
- The default value of the **limit** parameter for pagination has been reduced from **100** to **10**. The max value of the **limit** parameter for pagination has been reduced from **100** to **50**.

1.7.0
----------------
- Entity Create API Created
- Entity Type List API Created
- E360_API now has the "engagement/entities/dynamic_fields" endpoint.
- Added create endpoint, cypress test, and document of the engagement service point.
- Added type list endpoint, cypress test, and document of engagement service point.
- Added dynamic field list cypress test, and document of engagement service point.

1.8.0
----------------
- A service is created to return Task Details.
- Order Detail service has been developed for E360 API.
- A service is created to return Task Transitions.
- OpenAPI endpoint for announcements is created to list both announcements for the registered client, and the announcements with no client id.
- A service is created to return Task Step Details.

1.8.1
----------------
- A service is created to return Order List.

1.9.0
----------------
- Task List endpoint added.
- API endpoint for displaying client bounds is configured. The response consists of the tile provider and a bound dictionary of north_east, south_west coordinate points. Each coordinate point consists of lat, lon. If the client does not have that module, bounds are provided as null.
- The API endpoint for creating an order does not require a name, hence the field is made optional.
- The API endpoint for listing cases is configured. The user can now optionally filter cases based on entity_id, service_point_id, contact_id, and case_type_id. Additionally, the results can be ordered by ascending or descending created_at dates.

1.10.0
----------------
- Status color added to case list service response.

1.10.1
----------------
- Added "order_type_ids" parameter to :doc:`Engagement ServicePoint <engagement/service_availability/post_v2>`.