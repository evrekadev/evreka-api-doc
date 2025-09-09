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

1.11.0
----------------
- Enabled searching with multiple service_point_id and multiple entity_id. Users can now send comma separated ids to get the union of the results of those ids.
- Corresponding services for editing attachments are added to Engagement and API modules. Users can now add or delete attachments by providing files or attachment ids respectively.

1.12.0
----------------
- Refactored slow methods within the endpoint to eliminate timeouts and significantly improve response times.
- Service points, along with their related orders and cases, can now be deleted through the API.
- Added options for filtering service point types using the extra field with custom parameters, enabling more flexible queries.
- Dynamic fields support has been implemented for MRF activities. As part of this update, headers and keys have been renamed for improved clarity. Dynamic fields can now be retrieved through a dedicated endpoint, and any newly added fields are not displayed by default.

1.13.0
----------------
- Entity type can be filtered by custom fields on the extra field. 
- Uniqueness validation is added for phone numbers and emails. If the given phone number/email is used by another user, there will be an error stating that.

1.14.0
----------------
- Contacts of the selected order will be shown in the detail.
- Contacts can be given as a UUID list parameter in create order API endpoint.
- Points per UOM can be shown based on the 'include_points' parameter as part of the request.

1.15.0
----------------
- Notes can be added now as part of the request while creating order via OpenAPI.
- Service availability endpoint is revised to include order type in the response.

1.16.0
----------------
- status_id, sort_key and sort_order params added to order list document
- completion_time added to Order model. It is saved when the order status changes to completed. Returned in order list api service
- Parcel API Created, Task API optional parameter "inbound_id" added to get linked objects
- Branch list API service has been developed. 

1.17.0
----------------
- Corresponding Operations Management service point and its linked Engagement service points will be returned when asset_tag is provided.
- Inbound outages endpoint now returns a dictionary with two arrays: items and types. MRF dynamic fields can now be retrieved by specifying a content_type in the URL path.

1.19.0
----------------
- Service Point Edit endpoint is added into OpenAPI services, enabling users to edit service points by external requests from the API.
- Language field added into contact model and related Engagement and OpenAPI services.
- Completion_time_start and completion_time_end parameters added to filter completed orders in this range.