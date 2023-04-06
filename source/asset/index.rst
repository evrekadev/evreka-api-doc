Asset Management
=================

Asset Types
----------------

Data Structure
^^^^^^^^^^^^^^^^^

.. table::
   :width: 100%

   +-------------------+--------------+------------------+
   | Field Name        | Data Type    | Description      |
   +===================+==============+==================+
   | id                | int          | Asset Type ID    |
   +-------------------+--------------+------------------+
   | name              | string       | Asset Type Name  |
   +-------------------+--------------+------------------+

Example Request
^^^^^^^^^^^^^^^^^

.. code-block:: python

   EVREKA360_API_USER = ""
   EVREKA360_API_PASS = ""
   EVREKA360_BASE_URL = "https://api.360.evreka.co"

   session = requests.session()
   session.auth = (EVREKA360_API_USER, EVREKA360_API_PASS)

   service_url = "/asset/types"
   headers = {"Content-Type": "application/json; charset=utf-8"}

   resp = session.get(EVREKA360_BASE_URL + service_url, headers=headers)
   print(resp.status_code, resp.json())

Asset Statuses
----------------

Data Structure
^^^^^^^^^^^^^^^^^

.. table::
   :width: 100%

   +-------------------+--------------+------------------+
   | Field Name        | Data Type    | Description      |
   +===================+==============+==================+
   | id                | int          | Status ID        |
   +-------------------+--------------+------------------+
   | name              | string       | Status Name      |
   +-------------------+--------------+------------------+
   | color             | string       | Status Color     |
   +-------------------+--------------+------------------+
   | location          | string       | Status Locations |
   +-------------------+--------------+------------------+

Example Request
^^^^^^^^^^^^^^^^^

.. code-block:: python

   EVREKA360_API_USER = ""
   EVREKA360_API_PASS = ""
   EVREKA360_BASE_URL = "https://api.360.evreka.co"

   session = requests.session()
   session.auth = (EVREKA360_API_USER, EVREKA360_API_PASS)

   service_url = "/asset/statuses"
   headers = {"Content-Type": "application/json; charset=utf-8"}

   resp = session.get(EVREKA360_BASE_URL + service_url, headers=headers)
   print(resp.status_code, resp.json())

Asset Status Locations
-------------------------

ENUM
^^^^^^^^^^^^^^^^^

.. table::
   :width: 100%

   +-------------------+------------------+
   | Key               | Value            |
   +===================+==================+
   | route             | In Route         |
   +-------------------+------------------+
   | service_point     | Service Point    |
   +-------------------+------------------+
   | mrf               | MRF              |
   +-------------------+------------------+
   | parcel            | Parcel           |
   +-------------------+------------------+
   | gps               | GPS              |
   +-------------------+------------------+

Asset List
----------------


Asset Detail
----------------


Asset Activity Categories
---------------------------

Data Structure
^^^^^^^^^^^^^^^^^

.. table::
   :width: 100%

   +-------------------+--------------+------------------+
   | Field Name        | Data Type    | Description      |
   +===================+==============+==================+
   | id                | int          |                  |
   +-------------------+--------------+------------------+
   | name              | string       |                  |
   +-------------------+--------------+------------------+
   | enum              | string       |                  |
   +-------------------+--------------+------------------+

Example Request
^^^^^^^^^^^^^^^^^

.. code-block:: python

   EVREKA360_API_USER = ""
   EVREKA360_API_PASS = ""
   EVREKA360_BASE_URL = "https://api.360.evreka.co"

   session = requests.session()
   session.auth = (EVREKA360_API_USER, EVREKA360_API_PASS)

   service_url = "/asset/activities/categories"
   headers = {"Content-Type": "application/json; charset=utf-8"}

   resp = session.get(EVREKA360_BASE_URL + service_url, headers=headers)
   print(resp.status_code, resp.json())

Asset Activity Types
---------------------------

Data Structure
^^^^^^^^^^^^^^^^^

.. table::
   :width: 100%

   +-------------------+--------------+-----------------------------+
   | Field Name        | Data Type    | Description                 |
   +===================+==============+=============================+
   | id                | int          |                             |
   +-------------------+--------------+-----------------------------+
   | name              | string       |                             |
   +-------------------+--------------+-----------------------------+
   | enum              | string       |                             |
   +-------------------+--------------+-----------------------------+
   | category_id       | int          | Asset Activity Category ID  |
   +-------------------+--------------+-----------------------------+

Example Request
^^^^^^^^^^^^^^^^^

.. code-block:: python

   EVREKA360_API_USER = ""
   EVREKA360_API_PASS = ""
   EVREKA360_BASE_URL = "https://api.360.evreka.co"

   session = requests.session()
   session.auth = (EVREKA360_API_USER, EVREKA360_API_PASS)

   service_url = "/asset/activities/types"
   headers = {"Content-Type": "application/json; charset=utf-8"}

   resp = session.get(EVREKA360_BASE_URL + service_url, headers=headers)
   print(resp.status_code, resp.json())

Asset Activities
----------------

Data Structure
^^^^^^^^^^^^^^^^^

.. table::
   :width: 100%

   +------------------------------+----------------------------------------------------------------------------------+------------------------------------------+
   | Field Name                   | Data Type                                                                        | Description                              |
   +==============================+==================================================================================+==========================================+
   | id                           | `ObjectId <https://www.mongodb.com/docs/manual/reference/method/ObjectId/>`_     |                                          |
   +------------------------------+----------------------------------------------------------------------------------+------------------------------------------+
   | activity_category_id         | int                                                                              | Asset Activity Category                  |
   +------------------------------+----------------------------------------------------------------------------------+------------------------------------------+
   | activity_type_id             | int                                                                              | Asset Activity Type                      |
   +------------------------------+----------------------------------------------------------------------------------+------------------------------------------+
   | after_value                  | mixed                                                                            |                                          |
   +------------------------------+----------------------------------------------------------------------------------+------------------------------------------+
   | before_value                 | mixed                                                                            |                                          |
   +------------------------------+----------------------------------------------------------------------------------+------------------------------------------+
   | asset_id                     | int                                                                              |                                          |
   +------------------------------+----------------------------------------------------------------------------------+------------------------------------------+
   | source_name                  | string                                                                           |                                          |
   +------------------------------+----------------------------------------------------------------------------------+------------------------------------------+
   | payload                      | dict *(nullable)*                                                                |                                          |
   +------------------------------+----------------------------------------------------------------------------------+------------------------------------------+
   | activity_time                | `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_                             |                                          |
   +------------------------------+----------------------------------------------------------------------------------+------------------------------------------+
   | created_at                   | `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_                             |                                          |
   +------------------------------+----------------------------------------------------------------------------------+------------------------------------------+

Example Request
^^^^^^^^^^^^^^^^^

.. code-block:: python

   EVREKA360_API_USER = ""
   EVREKA360_API_PASS = ""
   EVREKA360_BASE_URL = "https://api.360.evreka.co"

   session = requests.session()
   session.auth = (EVREKA360_API_USER, EVREKA360_API_PASS)

   service_url = "/asset/activities/list"
   headers = {"Content-Type": "application/json; charset=utf-8"}

   resp = session.get(EVREKA360_BASE_URL + service_url, headers=headers)
   print(resp.status_code, resp.json())
