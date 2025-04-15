Edit Case Attachments API
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | POST              | ``/cases/{case_id}/edit_attachments``      |
   +-------------------+--------------------------------------------+

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
    | attachments_tbd         | list object *(optional)*                                     | List of Case Attachment ID - UUID                 | ``["009f40a6-1dd5-4380-97b5-8b0d406ee45a"]``          |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    case_id = "9a97a833-aad7-4c51-9a66-501492e20d1b"

    service_url = "/engagement/cases/" + case_id + "/edit_attachments"
    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    # Data Example #1
    data = {
        "attachments_tbd": [
            "009f40a6-1dd5-4380-97b5-8b0d406ee45a"
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
        "detail": "Attachments updated successfully"
    }
    

*Status Code:* ``400`` - Bad Request
*Content Type:* ``application/json``
*Body:*

.. code-block:: json 

    {
        "detail": "Failed to update attachments."
    }

*Status Code:* ``404`` - Not Found
*Content Type:* ``application/json``
*Body:*


.. code-block:: json

    {
        "detail": "Case ({case_id}) not found"
    }

