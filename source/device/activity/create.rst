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

.. table::
    :width: 100%

    +---------------------+-----------------------------------------------------------------------+-------------------------------------------------+
    | Field Name          | Data type                                                             | Description                                     |
    +=====================+=======================================================================+=================================================+
    | transaction_id      | int *(required)*                                                      | Unique identifier for the transaction           |
    +---------------------+-----------------------------------------------------------------------+-------------------------------------------------+
    | trace_id            | int *(optional)*                                                      | Identifier for tracing the transaction          |
    +---------------------+-----------------------------------------------------------------------+-------------------------------------------------+
    | vehicle_identifier  | string *(optional)*                                                   | Unique identifier for the vehicle               |
    +---------------------+-----------------------------------------------------------------------+-------------------------------------------------+
    | asset_identifier    | string *(optional)*                                                   | Unique identifier for the asset                 |
    +---------------------+-----------------------------------------------------------------------+-------------------------------------------------+
    | gross_weight        | float *(optional)*                                                    | Gross weight of the asset or vehicle            |
    +---------------------+-----------------------------------------------------------------------+-------------------------------------------------+
    | tare_weight         | float *(optional)*                                                    | Tare weight of the asset or vehicle             |
    +---------------------+-----------------------------------------------------------------------+-------------------------------------------------+
    | net_weight          | float *(optional)*                                                    | Net weight calculated as gross minus tare weight|
    +---------------------+-----------------------------------------------------------------------+-------------------------------------------------+
    | is_contaminated     | bool *(optional)*                                                     | Indicates if the asset is contaminated          |
    +---------------------+-----------------------------------------------------------------------+-------------------------------------------------+
    | gross_timestamp     | `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_ *(optional)*     | time when the gross weight was recorded         |
    +---------------------+-----------------------------------------------------------------------+-------------------------------------------------+
    | tare_timestamp      | `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_ *(optional)*     | time when the tare weight was recorded          |   
    +---------------------+-----------------------------------------------------------------------+-------------------------------------------------+
    | waste_type_id       | int *(optional)*                                                      | Waste Type ID related with weighing             |
    +---------------------+-----------------------------------------------------------------------+-------------------------------------------------+
    | media               | UploadFile *(optional)*                                               | Media file associated with the transaction      |    
    +---------------------+-----------------------------------------------------------------------+-------------------------------------------------+

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
        "vehicle_identifier": "ABC123XYZ",
        "asset_identifier": "ASSET456",
        "gross_weight": 1000.45,
        "tare_weight": 300.5,
        "net_weight": 699.95,
        "is_contaminated": False,
        "gross_timestamp": "2023-10-01T12:00:00Z",
        "tare_timestamp": "2023-10-01T12:30:00Z",
        "waste_type_id": 1,
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

