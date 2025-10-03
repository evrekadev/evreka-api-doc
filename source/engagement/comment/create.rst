Create Comment API
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | POST              | ``/comments``                              |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^

``case_id``,  ``user_id`` and ``description`` must be provided.

.. table::
    :width: 100%

    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | Field Name              | Data Type                                                    | Description                                       | Value                                                                              |
    +=========================+==============================================================+===================================================+====================================================================================+
    | case_id                 | string *(required)*                                          | Case ID - UUID                                    | d666a904-5739-46c0-b70a-1cd57658a3f6                                               |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | user_id                 | int *(required)*                                             | User ID                                           | 123                                                                                |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | description             | string *(required)*                                          | Description                                       | This is a comment                                                                  |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+
    | attachments             | File *(optional)*                                            | Comment Attachments                               | my_attachment.png                                                                  |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------+

.. |br| raw:: html

      <br>

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests
    import json

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/engagement/comments"
    headers = {
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    # Data Example
    data = {
        "case_id": "d666a904-5739-46c0-b70a-1cd57658a3f6",
        "user_id": 123,
        "description": "This is a comment",
    }

    # File Data Example
    files = {
        "attachments": ("<file_name>", open("<file_name>", "rb"), "<file_type>")
    }

    resp = requests.post(EVREKA360_API_BASE_URL + service_url, headers=headers, data=data, files=files)
    print(resp.status_code, resp.json())

Response
^^^^^^^^^^^^^^^^^
*Status Code:* ``200`` - Retrieved successfully

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

    {
        "id": "COMMENT ID",
        "case_name": "CASE NAME",
        "created_at": "CREATE TIME",
    }

*Status Code:* ``400`` - Bad request

*Content Type:* ``application/json``

*Body:*

.. code-block:: json


    {
        "detail":"An error occurred while creating the Comment"
    }

