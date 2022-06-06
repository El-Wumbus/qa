Usage
=====

This program has two functions: ``load`` and ``unload``. 
loading meaning "compress with a plain text file containing the full path of what directory was compressed,
and unloading meaning decompress to the location in that plain text file.

qa load
***********

This function takes three arguments.
The function declaration:

.. code:: python

   def load(archive_dir: str, archive_name: str, mode: str):

- ``archive_dir`` is the directory targeted for compression. (i.e. ``$HOME/.config``) 
- ``archive_name`` is the name of the desired archive file. (i.e. ``config.tar.xz``)
- ``mode`` is the compression type desired for the file. (i.e. ``xz``)

Example:
~~~~~~~~

.. code:: bash

   qa load "$HOME/.config" config.tar.xz xz
.. pull-quote::

  If this archive were to be unloaded it would be extracted to ``$HOME/.config`` 

qa unload
*************

This Function takes one argument. 
The function declaration:

.. code:: python

   def unload(archive_name: str):

- ``archive_name`` is the archive targeted for decompression. 
  
The archive gets decompressed to the directory that was original compressed.

Example:
~~~~~~~~

.. code:: bash

   qa unload config.tar.xz
