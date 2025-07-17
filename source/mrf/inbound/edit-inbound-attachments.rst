Edit Inbound Attachments API
-----------------------------------

.. table::

   +-------------------+-------------------------------------------------+
   | POST              | ``/inbounds/{inbound_id}/edit_attachments``     |
   +-------------------+-------------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
Request content type should be multipart/form-data.


.. table::
    :width: 100%

    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
    +=========================+==============================================================+===================================================+=======================================================+
    | attachments             | file *(optional)*                                            | A list of files uploaded via multipart/form-data  | ``my_attachment.png``                                 |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | attachments_tbd         | list object *(optional)*                                     | List of Inbound Attachment ID - Integer           | ``["243"]``                                           |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    inbound_id = 69212

    service_url = "/mrf/inbounds/" + inbound_id + "/edit_attachments"
    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    # Data Example #1
    data = {
        "attachments_tbd": [
            "243"
        ]
    }

    files = [
        ('attachments', ('sample.jpg', open('<path-to-sample.jpg>', 'rb'), 'image/jpeg')),
        ('attachments', ('sample2.jpg', open('<path-to-sample2.jpg>', 'rb'), 'image/jpeg')),
        ('attachments', ('sample3.jpg', open('<path-to-sample3.jpg>', 'rb'), 'image/jpeg'))
    ]

    resp = requests.post(EVREKA360_API_BASE_URL + service_url, headers=headers, data=data, files=files)
    print(resp.status_code, resp.json())

Response
^^^^^^^^^^^^^^^^^
*Status Code:* ``200`` - Retrieved successfully
*Content Type:* ``application/json``
*Body:*


.. code-block:: json 

    {
        "success" : "Boolean",
        "inbound_id" : "Inbound ID - Integer",
        "detail": "Media attached/detached to Incoming ({inbound.name)} successfully"
    }
    


*Status Code:* ``404`` - Not Found
*Content Type:* ``application/json``
*Body:*


.. code-block:: json

    {
        "detail": "Inbound ({inbound_id}) not found"
    }

