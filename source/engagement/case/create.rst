Create Case API
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | POST              | ``/cases``                                 |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
If name field is not provided, name will be generated automatically.
One of the following fields must be provided: entity_id, type_id and subject. 
If any required dynamic field exists for the contact, it must be provided in the request.

.. table::
    :width: 100%

    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
    +=========================+==============================================================+===================================================+=======================================================+
    | name                    | string *(optional)*                                          | Name                                              | CaseName                                              |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | type_id                 | string *(required)*                                          | Case Type ID - UUID                               | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | sub_type_id             | string *(optional)*                                          | Sub Case Type ID - UUID                           | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | status_id               | string *(optional)*                                          | Case Status ID - UUID                             | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | entity_id               | string *(required)*                                          | Entity ID - UUID                                  | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | contact_id              | string *(optional)*                                          | Contact ID - UUID                                 | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | service_point_id        | string *(optional)*                                          | Service Point ID - UUID                           | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | subject                 | string *(required)*                                          | Subject                                           | CaseSubject                                           |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | description             | string *(optional)*                                          | Description                                       | CaseDescription                                       |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | assignee_id             | integer *(optional)*                                         | Assignee ID                                       | 15                                                    | 
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | corrective_action       | string *(optional)*                                          | Corrective Action                                 | CaseCorrectiveAction                                  |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | notify_contact          | boolean *(optional)*                                         | Notify Contact                                    | true                                                  |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | latitude                | float *(optional)*                                           | Latitude                                          | 12.12345                                              |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | longitude               | float *(optional)*                                           | Longitude                                         | 12.12345                                              |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | dynamic_field_list      | list object *(optional)*                                     | Object contains dynamic field key and value       | ``[{"key":"numberField","value": 123"}]``             |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/engagement/cases"
    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    # Data Example #1
    data = {
        "name": "Case Name",
        "type_id": "TYPE_ID_UUID",
        "sub_type_id": "SUB_TYPE_ID_UUID",
        "status_id": "STATUS_ID_UUID",
        "entity_id": "ENTITY_ID_UUID",
        "contact_id": "CONTACT_ID_UUID",
        "service_point_id": "SERVICE_POINT_ID_UUID",
        "subject": "Case Subject",
        "description": "Case Description",
        "assignee_id": 1,
        "corrective_action": "Case Corrective Action",
        "notify_contact": true,
        "latitude": 12.12345,
        "longitude": 12.12345,
        "dynamic_field_list": [
            {
                "key": "numberField",
                "value": 123
            }
        ]
        }

    resp = requests.post(EVREKA360_API_BASE_URL + service_url, headers=headers, json=data)
    print(resp.status_code, resp.json())

Response
^^^^^^^^^^^^^^^^^
*Status Code:* ``200`` - Retrieved successfully
*Content Type:* ``application/json``
*Body:*

.. code-block:: json 

    {
        "contact_id": "CONTACT_ID_UUID",
        "case_id": "CASE_ID_UUID",
        "case_name": "Case Name",
        "case_type_id": "CASE_TYPE_ID_UUID",
        "case_type_name": "Case Type Name",
        "case_status_id": "CASE_STATUS_ID_UUID",
        "case_status_name": "Case Status Name",
        "case_author": "AUTHOR_NAME",
        "case_contact_name": "CONTACT_NAME",
        "message": "MESSAGE",
    }
    
.. code-block:: tex

Status Code:* ``400`` - Bad request
*Content Type:* ``application/json``
*Body:*

.. code-block:: json


    {
        "detail":"An error occurred while creating the Case"
    }

