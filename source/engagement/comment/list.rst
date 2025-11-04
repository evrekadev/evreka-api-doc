Comment List
----------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/comments``                              |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^

.. table::

   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+---------------------------------------------------------------------------+
   | Field Name              | Data Type                                                    | Description                                       | Value                                                                     |
   +=========================+==============================================================+===================================================+===========================================================================+
   | case_id                 | string *(optional)*                                          | Case ID - UUID                                    | d666a904-5739-46c0-b70a-1cd57658a3f6                                      |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+---------------------------------------------------------------------------+
   | is_internal             | boolean *(optional)*                                         | Internal comments only                            | True                                                                      |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+---------------------------------------------------------------------------+

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/engagement/comments"
    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    # filter example #1: is_internal
    #service_url += "?is_internal=True"
    
    # filter example #2: to use multiple filters, use the & character between the filters.
    #service_url += "?is_internal=True" + "&case_id=d666a904-5739-46c0-b70a-1cd57658a3f6"

    resp = requests.get(EVREKA360_API_BASE_URL + service_url, headers=headers)
    print(resp.status_code, resp.json())

Response
^^^^^^^^^^^^^^^^^
*Status Code:* ``200`` - Retrieved successfully
*Content Type:* ``application/json``
*Body:*

.. code-block:: json 

    {
        "items": [
            {
                "id": "Comment ID - UUID",
                "user": "Comment User - String",
                "contact_id": "Contact ID - UUID",
                "description": "Comment Description - String",
                "is_internal": "Is Internal - Boolean",
                "created_at": "Created At - ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>",
                "updated_at": "Updated At - ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>",
                "attachments": [
                    {
                        "id": "Attachment ID - UUID",
                        "media_name": "Attachment Media Name - String",
                        "media_url": "Attachment Media URL - String"
                    }
                ]
            }
        ]
    }