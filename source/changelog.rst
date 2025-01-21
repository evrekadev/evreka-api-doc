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
