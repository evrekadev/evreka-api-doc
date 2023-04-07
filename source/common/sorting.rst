Sorting
=================

Like pagination, all "List" endpoints have sorting options. Type of sorting depends on the data returned with the result set. Definitions below are for date sorting, that most of the "List" endpoints support.

.. table::
   :width: 100%

   +-------------------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Field Name        | Type         | Description                                                                                                                                           |
   +===================+==============+=======================================================================================================================================================+
   | sort              | string       | For most of the "List" endpoints sort is an optional query parameter. For instance, for sorting dates these enums are used. |br|                      |
   |                   |              | field-desc: Results are sorted by ``field`` descending. |br|                                                                                          |
   |                   |              | field-asc: Results are sorted by ``field`` ascending. |br|                                                                                            |
   |                   |              | |br|                                                                                                                                                  |
   |                   |              | Default: create_time-desc                                                                                                                             |
   +-------------------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+


.. |br| raw:: html

      <br>