.. raw:: pdf

   PageBreak

Delete Service Point API
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | DELETE            | ``/service_points/{service_point_id}``     |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
Service Point ID is required UUID for the service point to be deleted.
If ``should_delete_linked_cases`` and/or ``should_delete_linked_orders`` are set to ``true``, all linked cases and/or orders will be deleted as well.


.. table::

   +---------------------------------+----------------------+------------------------------------+
   | Field                           | Data Type            | Description                        |
   +=================================+======================+====================================+
   | should_delete_linked_cases      | boolean *(optional)* | if linked cases should be deleted  |
   +---------------------------------+-------------------+---------------------------------------+
   | should_delete_linked_orders     | boolean *(optional)* | if linked orders should be deleted |
   +---------------------------------+----------------------+------------------------------------+

Example Code
^^^^^^^^^^^^^^^^^
.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    #Example data (optional body)
    data = { 
        "should_delete_linked_cases": True,
        "should_delete_linked_orders": True
    }
    # Data Example 2
    # data = {
    #     "should_delete_linked_cases": True,
    # }

    # Data Example 3
    # data = {
    #     "should_delete_linked_orders": True,
    # }

    # Data Example 4
    # data = {}

    service_point_id = ""
    service_url = "/engagement/service_points/" + service_point_id
    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    resp = requests.delete(EVREKA360_API_BASE_URL + service_url, headers=headers, json=data)
    print(resp.status_code, resp.json())


Response
^^^^^^^^^^^^^^^^^

*Status Code:* ``200`` - Retrieved successfully
*Content Type:* ``application/json``
*Body:*

.. code-block:: json 

    {
        "detail": "Successfully deleted Service Point ({service_point_name})"
    }

*Status Code:* ``404`` - Not Found
*Content Type:* ``application/json``
*Body:*

.. code-block:: json 

    {
        "detail": "Service Point ({service_point_id}) not found"
    }

