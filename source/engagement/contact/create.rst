Create Contact API
-----------------------------------

.. table::

   +-------------------+--------------------------------------------+
   | POST               | ``/contacts``                             |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^
One of the following fields must be provided: entity_id name and surname. 
If any required dynamic field exists for the contact, it must be provided in the request.

.. table::
    :width: 100%

    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
    +=========================+==============================================================+===================================================+=======================================================+
    | name                    | string *(required)*                                          | Name                                              | ContactName                                           |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | entity_id               | string *(required)*                                          | Entity ID - UUID                                  | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | surname                 | string *(required)*                                          | Surname                                           | ContactSurname                                        |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | email                   | string *(optional)*                                          | Email                                             | test@test.com                                         |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | phone                   | string *(optional)*                                          | Phone Number                                      | 782347632476                                          |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | language                | string *(optional)*                                          | Language Code                                     | en                                                    |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | service_point_id_list   | list *(optional)*                                            | Service Point ID List - UUID                      | [d666a904-5739-46c0-b70a-1cd57658a3f6]                |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | dynamic_field_list      | list object *(optional)*                                     | Object contains dynamic field key and value       | ``[{"key":"numberField",``                            |
    |                         |                                                              |                                                   | ``"value": 123"}]``                                   | 
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
    | has_customer_portal     | boolean *(optional)*                                         | Has Customer Portal                               | true                                                  |
    +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+

Example Code
^^^^^^^^^^^^^^^^^

.. code-block:: python

    import requests

    EVREKA360_API_BASE_URL = ""
    ACCESS_TOKEN = ""

    service_url = "/engagement/contacts"
    headers = {
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Bearer " + ACCESS_TOKEN
    }

    # Data Example #1
    data = {
        "entity_id": "ENTITY_ID_UUID",
        "name": "Contact Name",
        "surname": "Contact Surname",
        "email": "test@test.com",
        "phone": "782347632476",
        "language": "nl",
        "service_point_id_list": [
            "SERVICE_POINT_ID_UUID"
        ],
        "dynamic_field_list": [
            {
                "key": "numberField",
                "value": 123
            }
        ],
        "has_customer_portal": true
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
        "name": "Contact Name",
        "surname": "Contact Surname",
        "entity_name": "Entity Name"
    }
    
.. code-block:: tex

Status Code:* ``400`` - Bad request
*Content Type:* ``application/json``
*Body:*

.. code-block:: json


    {
        "detail":"An error occurred while creating the Contact"
    }

