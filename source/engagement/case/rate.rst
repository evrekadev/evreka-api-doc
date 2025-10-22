Case Rate API
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | POST              | ``/cases/{case_id}/rate``                  |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
Request content type should be application/json.


.. table::
    :width: 100%

    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
    +=========================+==============================================================+===================================================+=======================================================+
    | rate                    | integer *(required)*                                         | Rate of the case (1-5)                            | 5                                                     |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | rate_note               | string *(optional)*                                          | Rate note of the case (required for rate 1-3)     | Good job!                                             |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    case_id = "9a97a833-aad7-4c51-9a66-501492e20d1b"

    service_url = "/engagement/cases/" + case_id + "/rate"
    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    # Data Example #1
    data = {
        "rate": 5
    }

    # Data Example #2
    data = {
        "rate": 3,
        "rate_note": "Good job!" # This is required for rate 1-3
    }



    resp = requests.post(EVREKA360_API_BASE_URL + service_url, headers=headers, data=data)
    print(resp.status_code, resp.json())

Response
^^^^^^^^^^^^^^^^^
*Status Code:* ``200`` - Retrieved successfully
*Content Type:* ``application/json``
*Body:*


.. code-block:: json 

    {
        "success" : "Boolean",
        "case_id" : "Case ID - UUID",
    }
    

*Status Code:* ``400`` - Bad Request
*Content Type:* ``application/json``
*Body:*

.. code-block:: json 

    {
        "detail": "Client does not have case rate permission"
    }


*Status Code:* ``404`` - Not Found
*Content Type:* ``application/json``
*Body:*


.. code-block:: json

    {
        "detail": "Case ({case_id}) not found"
    }

