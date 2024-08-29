Contact List
----------------

.. table::

   +-------------------+--------------------------------------------+
   | GET               | ``/contacts``                              |
   +-------------------+--------------------------------------------+

Data Structure
^^^^^^^^^^^^^^^^^

.. table::

   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | Field Name              | Data Type                                                    | Description                                       | Value                                                 |
   +=========================+==============================================================+===================================================+=======================================================+
   | name                    | string *(optional)*                                          | Contact Name                                      | MyContact                                             |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | entity_id               | string *(optional)*                                          | Contact Entity ID - UUID                          | d666a904-5739-46c0-b70a-1cd57658a3f6                  |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | surname                 | string *(optional)*                                          | Contact Surname                                   | MySurname                                             |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | email                   | string *(optional)*                                          | Contact Email                                     | my@email.com                                          |
   +-------------------------+--------------------------------------------------------------+---------------------------------------------------+-------------------------------------------------------+
   | phone                   | string *(optional)*                                          | Contact Phone                                     | +1234567890                                           |
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
    
    # filter example #1
    #service_url += "?page=1&limit=10"

    # filter example #2
    #service_url += "?name=MyEntity"

    # filter example #3
    #service_url += "?type_id=d666a904-5739-46c0-b70a-1cd57658a3f6"

    # filter example #4 
    #service_url += "?postcode=1234AB"

    # filter example #5 #To use multiple filters, use the & character between the filters.
    #service_url += "?name=MyServicePointName" + "&postcode=1234AB"

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
                "name": "Contact Name",
                "surname": "Contact Surname",
                "email": "Contact Email",
                "phone": "Contact Phone",
                "entity_id": "Entity UUID",
                "has_customer_portal": "true/false",
                "service_point_id_list": "Service Point UUID",
                "dynamic": "Dynamic Field JSON"
            }
        ]
    }
