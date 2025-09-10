Environment
--------------------------

.. table::

   +-------------------+------------------------------------------------+
   | GET               | ``/environment``                               |
   +-------------------+------------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
There is no required parameter for this request.


Example Code
^^^^^^^^^^^^

.. code-block:: python

   import requests
   EVREKA360_API_BASE_URL = ""
   ACCESS_TOKEN = ""
   service_url = "/engagement/environment"
   headers = {
       "Content-Type": "application/json; charset=utf-8",
       "Authorization": "Bearer " + ACCESS_TOKEN
   }

   resp = requests.get(EVREKA360_API_BASE_URL + service_url, headers=headers)
   print(resp.status_code, resp.json())

Response
^^^^^^^^^^^^^^^^^

*Status Code:* ``200`` - Retrieved successfully

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

   {
        "client_id": "Client ID - UUID",
        "client_name": "Client Name - String",
        "availability_start_offset_days": "Availability Start Offset Days - Integer",
   }
