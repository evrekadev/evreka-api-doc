QR Code API List
======================

.. toctree::
   :maxdepth: 2
   :caption: QR Code

   create
   verify
   public_keys

This part provides documentation for available API endpoints of QR Code Model for Engagement Module.

QR codes are short-lived, signed identity tokens issued for a contact. The token is rendered as a QR code by the client application and scanned by field devices, collection applications or partner applications to identify the contact without sharing any personal data.

Tokens are signed JWTs (``ES256``). They can be verified online with the verify endpoint or offline with the published public keys.


.. table::
   :width: 100%

   +--------+-----------------------+-----------------------------------------------+
   | Method | Endpoint              | Description                                   |
   +========+=======================+===============================================+
   | POST   | /qr_codes             | Create a QR code token for the given contact  |
   +--------+-----------------------+-----------------------------------------------+
   | POST   | /qr_codes/verify      | Verify a scanned QR code token                |
   +--------+-----------------------+-----------------------------------------------+
   | GET    | /qr_codes/public_keys | Retrieve public keys for offline verification |
   +--------+-----------------------+-----------------------------------------------+
