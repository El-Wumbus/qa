QA
==

*quick archival.* A program that allows for single command compression
and extraction using ``xz``, ``gz``, and ``bz2`` compression

| This script compresses an archive of a directory that includes
  information of where the archive should be decompressed.
| This could be used for, as an example, dotfile installation.
| This is, of course, cross platform. I made this program in an effort
  to learn about file manipulation and working with archives within
  python, as well as a bit of fun.
| You may find support in the `discord
  server <https://discord.gg/8wBUFeGGY>`__

Installaton
===========

From Releases (Linux/Windows)
-----------------------------

Download the `latest
release <https://github.com/El-Wumbus/qa/releases/latest>`__ for your
platform. These are standalone, portable binary releases with the python
interpreter and dependencies included in the binary.

From Source (Linux/macOS)
-------------------------

Build Dependencies
~~~~~~~~~~~~~~~~~~

-  git (To clone the repo)
-  python3
-  pip

Build Instructions
~~~~~~~~~~~~~~~~~~

.. code:: bash

   git clone https://github.com/el-wumbus/qa.git
   cd ./qa
   pip3 -r requirements.txt
   make
   sudo make install

From Source (Windows)
---------------------

.. _build-dependencies-1:

Build Dependencies
~~~~~~~~~~~~~~~~~~

-  `git <https://github.com/git-for-windows/git/releases/latest>`__ (To
   clone the repo)
-  `python3 <https://www.python.org/downloads/windows/>`__
-  `pip <https://pip.pypa.io/en/stable/installation/>`__

.. _build-instructions-1:

Build Instructions
~~~~~~~~~~~~~~~~~~

.. code:: powershell

   git clone "https://github.com/el-wumbus/qa"
   Set-Locaton .\qa
   pip3 -r requirements.txt
   pyinstaller --onefile src\qa.py
   cp dist\qa.exe .

The portable executable is located in the current directory.

Usage
-----

-  ``qa load`` - Takes three arguments.

The function declaration:

.. code:: python

   def load(archive_dir: str, archive_name: str, mode: str):

| ``archive_dir`` is the directory targeted for compression.
  (i.e. ``$HOME/.config``) ``archive_name`` is the name of the desired
  archive file. (i.e. ``config.tar.xz``)
| ``mode`` is the compression type desired for the file. (i.e. ``xz``)
| An example of its usage:

.. code:: bash

   qa load "$HOME/.config" config.tar.xz xz

-  ``qa unload`` - Takes one argument.

The function declaration:

.. code:: python

   def unload(archive_name: str):

``archive_name`` is the archive targeted for decompression. The archive
gets decompressed to the directory that was original compressed.

.. code:: bash

   qa unload config.tar.xz

Development
-----------

| The code within this repository uses the `GPLv3
  license <https://github.com/El-Wumbus/qa/blob/Master/LICENSE>`__
| A link to the source code can be found
  `HERE <https://github.com/El-Wumbus/qa>`__

You may make pull requests to change documentation or source code. Find
more information on how to contribute in
`CONTRIBUTION <https://github.com/El-Wumbus/qa/blob/Master/CONTRIBUTION.rst>`__