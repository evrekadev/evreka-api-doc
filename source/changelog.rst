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
