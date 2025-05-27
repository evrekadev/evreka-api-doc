Contact API List
======================

.. toctree::
   :maxdepth: 2
   :caption: Contact

   create
   update
   list
   validate_phone
   validate_email
   

This part provides documentation for available API endpoints of Contact Model for Engagement Module.


.. table::
   :width: 100%

   +-----------+-------------------------------------+------------------------------------------------------+
   | Method    | Endpoint                            | Description                                          |
   +===========+=====================================+======================================================+
   | POST      | /contacts                           | Create an contact with given parameters              |
   +-----------+-------------------------------------+------------------------------------------------------+
   | PUT       | /contacts/{contact_id}              | Update the contact with given contact id             |
   +-----------+-------------------------------------+------------------------------------------------------+
   | GET       | /contacts                           | Retrive contact list of contact model                |
   +-----------+-------------------------------------+------------------------------------------------------+
   | GET       | /contacts/validate/phone            | Validate the phone number of contact for uniqueness  |
   +-----------+-------------------------------------+------------------------------------------------------+
   | GET       | /contacts/validate/email            | Validate the email of contact for uniqueness         |
   +-----------+-------------------------------------+------------------------------------------------------+