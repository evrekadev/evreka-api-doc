Authentication
++++++++++++++
All REST API queries require a valid **Basic** auth.


Example Code
================

.. code-block:: python

   EVREKA360_API_USER = ""
   EVREKA360_API_PASS = ""
   EVREKA360_BASE_URL = ""

   import requests
   session = requests.session()
   session.auth = (EVREKA360_API_USER, EVREKA360_API_PASS)

   service_url = "/status"
   headers = {"Content-Type": "application/json; charset=utf-8"}

   resp = session.get(EVREKA360_BASE_URL + service_url, headers=headers)
   print(resp.status_code, resp.json())