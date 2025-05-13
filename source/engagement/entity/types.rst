Entity Type List
--------------------------

.. table::

   +-------------------+------------------------------------------------+
   | GET               | ``/entities/types``                            |
   +-------------------+------------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
There is no required parameter for this request. Optionally, dynamic fields on ``extra`` can be used to filter the results.


Example Code
^^^^^^^^^^^^

.. code-block:: python

   import requests
   EVREKA360_API_BASE_URL = ""
   ACCESS_TOKEN = ""
   service_url = "/engagement/entities/types"
   headers = {
       "Content-Type": "application/json; charset=utf-8",
       "Authorization": "Bearer " + ACCESS_TOKEN
   }

    #Filters on the field "extra" with the given key and value
    # service_url+="?address=ankara"

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
               "id": "UUID",
               "name": "Type Name"
           }
       ]
   }
