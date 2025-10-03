.. raw:: pdf

   PageBreak

Create Activity API
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | POST              | ``/device/record/weighing``                |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
If transaction_id exists, it will be used to create the new activity from the last activity which has same transaction_id and only given parameters will be updated.

One of fields ``vehicle_identifier`` or ``asset_identifier`` must be provided.

In addition to the fields listed below, users can include custom fields. Each custom field should be given as a standard key-value pair alongside the predefined fields.

.. table::
    :width: 100%

    +---------------------+-----------------------------------------------------------------------+---------------------------------------------------+
    | Field Name          | Data type                                                             | Description                                       |
    +=====================+=======================================================================+===================================================+
    | transaction_id      | int *(required)*                                                      | Unique identifier for the transaction             |
    +---------------------+-----------------------------------------------------------------------+---------------------------------------------------+
    | trace_id            | int *(optional)*                                                      | Identifier for tracing the transaction            |
    +---------------------+-----------------------------------------------------------------------+---------------------------------------------------+
    | vehicle_identifier  | string *(optional)*                                                   | Fleet Vehicle ID (UUID) or Plate                  |
    +---------------------+-----------------------------------------------------------------------+---------------------------------------------------+
    | asset_identifier    | string *(optional)*                                                   | Unique identifier for the asset                   |
    +---------------------+-----------------------------------------------------------------------+---------------------------------------------------+
    | first_weight        | float *(optional)*                                                    | First weight of the asset or vehicle              |
    +---------------------+-----------------------------------------------------------------------+---------------------------------------------------+
    | second_weight       | float *(optional)*                                                    | Second weight of the asset or vehicle             |
    +---------------------+-----------------------------------------------------------------------+---------------------------------------------------+
    | net_weight          | float *(optional)*                                                    | Net weight calculated as first minus second weight|
    +---------------------+-----------------------------------------------------------------------+---------------------------------------------------+
    | is_contaminated     | bool *(optional)*                                                     | Indicates if the asset is contaminated            |
    +---------------------+-----------------------------------------------------------------------+---------------------------------------------------+
    | first_timestamp     | `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_ *(optional)*     | time when the first weight was recorded           |
    +---------------------+-----------------------------------------------------------------------+---------------------------------------------------+
    | second_timestamp    | `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_ *(optional)*     | time when the second weight was recorded          |   
    +---------------------+-----------------------------------------------------------------------+---------------------------------------------------+
    | waste_type_id       | int *(optional)*                                                      | Waste Type ID related with weighing               |
    +---------------------+-----------------------------------------------------------------------+---------------------------------------------------+
    | media               | UploadFile *(optional)*                                               | Media file associated with the transaction        |    
    +---------------------+-----------------------------------------------------------------------+---------------------------------------------------+

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/device/record/weighing"
    headers = {
        "Content-Type": "Content-Type: multipart/form-data", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    data = {
        "transaction_id": 12345,
        "trace_id": 67890,
        "vehicle_identifier": "06EVR06", # or "620f7679-7b4c-4781-adec-2fa92c2b6671"
        "asset_identifier": "ASSET456",
        "first_weight": 1000.45,
        "second_weight": 300.5,
        "net_weight": 699.95,
        "is_contaminated": False,
        "first_timestamp": "2025-10-03T12:00:00Z",
        "second_timestamp": "2025-10-03T12:30:00Z",
        "waste_type_id": 1,
        # "custom_temparature": 15.5
    }
    files = {
        "media": open("path/to/file.jpg", "rb")
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
        "trace_id": "11111-111111-11111-11111"
    }

*Status Code:* ``400`` - Bad request

*Content Type:* ``application/json``

*Body:*

.. code-block:: json


    {
        "detail":"UNEXPECTED_ERROR"
    }

