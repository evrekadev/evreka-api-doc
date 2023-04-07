Pagination
=================

All "List" endpoints return paginated results. When you make a call to any of the "List" endpoints there may be a lot of results to return. Therefore we paginate the results for making it easier to handle.

.. table::
   :width: 100%

   +-------------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Field Name        | Type         | Description                                                                                                                                          |
   +===================+==============+======================================================================================================================================================+
   | page              | int          | For all the "List" endpoints page is an optional query parameter. It specifies the page of results to return. |br|                                   |
   |                   |              | |br|                                                                                                                                                 |
   |                   |              | Default: 1 |br|                                                                                                                                      |
   |                   |              | Minimum: 1                                                                                                                                           |
   +-------------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
   | limit             | int          | For all the "List" endpoints limit is an optional query parameter. It specifies the maximum number of items to be returned in result set. |br|       |
   |                   |              | |br|                                                                                                                                                 |
   |                   |              | Default: 10 |br|                                                                                                                                     |
   |                   |              | Minimum: 1 |br|                                                                                                                                      |
   |                   |              | Maximum: 50                                                                                                                                          |
   +-------------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------+

.. |br| raw:: html

      <br>