.. raw:: pdf

   PageBreak

Delete Comment API
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | DELETE            | ``/comments/{comment_id}``                 |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
Comment ID is required UUID for the comment to be deleted.

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    comment_id = ""
    service_url = "/engagement/comments/" + comment_id
    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }
    
    resp = requests.delete(EVREKA360_API_BASE_URL + service_url, headers=headers)
    print(resp.status_code, resp.json())


Response
^^^^^^^^^^^^^^^^^

*Status Code:* ``200`` - Retrieved successfully
*Content Type:* ``application/json``
*Body:*

.. code-block:: json 

    {
        "detail": "Successfully deleted Comment ({comment_id})"
    }

*Status Code:* ``404`` - Not Found
*Content Type:* ``application/json``
*Body:*

.. code-block:: json 

    {
        "detail": "Comment ({comment_id}) not found"
    }