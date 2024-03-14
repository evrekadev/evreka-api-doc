Order Dynamic Field List
-------------------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/orders/dynamic_fields`                  |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
'template_id' and 'order_type_id' are used to filter the dynamic fields. If both are not provided, all dynamic fields will be returned. If both are provided, order_type_id will be used to filter the dynamic fields.

.. table::
    :width: 100%

    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
    +=========================+==============================================================+===================================================+=======================================================+
    | template_id             | string *(optional)*                                          | Order Template ID - UUID                          | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | order_type_id           | string *(optional)*                                          | Order Type ID - UUID                              | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+


Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

   service_url = f"/engagement/orders/dynamic_fields"
   headers = {"Content-Type": "application/json; charset=utf-8"}
   resp = session.get(EVREKA360_BASE_URL + service_url, headers=headers)

Response
^^^^^^^^^^^^^^^^^
*Status Code:* ``200`` - Retrieved successfully
*Content Type:* ``application/json``
*Body:*

.. code-block:: json

    {
        "items": [
            {
                "key": "test-dyn",
                "label": "Address",
                "default_value": null,
                "field_type": "TEXT",
                "order": 1,
                "options": null,
                "required": false,
                "editable": true,
                "displayable": false,
                "cp_user_allowed": true,
                "type_id": "ORDER TYPE ID - UUID", // If order_type_id is provided
                "template_id": "ORDER TEMPLATE ID - UUID",
            }
        ]
    }
