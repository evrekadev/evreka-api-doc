.. raw:: pdf

   PageBreak

Create Recognition API
-----------------------------------

.. table::

   +------+-------------------------+
   | POST | ``/device/recognition`` |
   +------+-------------------------+

Data Structure
^^^^^^^^^^^^^^^^^

The image must be sent as ``multipart/form-data``. Supported formats are JPEG and PNG, max file size is 5 MB.

When ``session_id`` is provided, the recognition result is linked to the session (e.g. a drop-off session opened with a QR code) and can be referenced later with ``recognition_id``.

.. table::
   :width: 100%

   +------------------+-------------------------------------------------------------------+-----------------------------------------+--------------------------------------+
   | Field Name       | Data Type                                                         | Description                             | Value                                |
   +==================+===================================================================+=========================================+======================================+
   | image            | UploadFile *(required)*                                           | Image of the object                     | photo.jpg                            |
   +------------------+-------------------------------------------------------------------+-----------------------------------------+--------------------------------------+
   | asset_identifier | string *(optional)*                                               | Asset where the image was taken         | ASSET456                             |
   +------------------+-------------------------------------------------------------------+-----------------------------------------+--------------------------------------+
   | session_id       | string *(optional)*                                               | Session to link the result - UUID       | 3f2a1b4c-5d6e-4f70-8a9b-0c1d2e3f4a5b |
   +------------------+-------------------------------------------------------------------+-----------------------------------------+--------------------------------------+
   | waste_type_ids   | array *(optional)*                                                | Accepted waste type IDs, all as default | [1, 4]                               |
   +------------------+-------------------------------------------------------------------+-----------------------------------------+--------------------------------------+
   | client_timestamp | `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_ *(optional)* | Time when the image was taken           | 2026-09-28T10:02:00Z                 |
   +------------------+-------------------------------------------------------------------+-----------------------------------------+--------------------------------------+

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/device/recognition"
    headers = {
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    data = {
        "asset_identifier": "ASSET456",
        "session_id": "3f2a1b4c-5d6e-4f70-8a9b-0c1d2e3f4a5b",
        "client_timestamp": "2026-09-28T10:02:00Z"
    }
    files = {
        "image": open("path/to/photo.jpg", "rb")
    }

    resp = requests.post(EVREKA360_API_BASE_URL + service_url, headers=headers, data=data, files=files)
    print(resp.status_code, resp.json())

Response
^^^^^^^^^^^^^^^^^

*Status Code:* ``200`` - Recognized successfully

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

    {
        "recognition_id": "9c8b7a6d-5e4f-4a3b-8c2d-1e0f9a8b7c6d",
        "accepted": true,
        "waste_type_id": 4,
        "label": "metal",
        "confidence": 0.96,
        "alternatives": [
            {
                "waste_type_id": 1,
                "label": "plastic",
                "confidence": 0.03
            }
        ],
        "created_at": "2026-09-28T10:02:01Z"
    }

*Status Code:* ``200`` - Rejected

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

    {
        "recognition_id": "1a2b3c4d-5e6f-4a7b-8c9d-0e1f2a3b4c5d",
        "accepted": false,
        "waste_type_id": null,
        "label": "unknown",
        "confidence": 0.41,
        "detail": "OBJECT_NOT_ACCEPTED"
    }

*Status Code:* ``400`` - Bad request

*Content Type:* ``application/json``

*Body:*

.. code-block:: json

    {
        "detail": "INVALID_IMAGE"
    }
