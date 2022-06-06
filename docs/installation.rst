Installaton
===========

``qa`` is a cross-platfrom application with slightly different
installation instructions depending on your OS

From PKGBUILDS (Arch Linux)
***************************

.. code:: bash 

   git clone https://github.com/el-wumbus/qa.git
   cd qa/PKGBUILDS
   
   # If you want to install from latest release
   cd qa-bin
   makepkg -si

   #If you want to compile from source
   cd qa-git
   makepkg -si
   
From `archlinux-repo <https://github.com/El-Wumbus/archlinux-repo>`__ (Arch Linux)
**********************************************************************************

Add the repo acording to `the instructions <https://github.com/El-Wumbus/archlinux-repo/blob/Master/README.md>`__
   
From Releases (Linux/Windows)
*****************************

Download the `latest
release <https://github.com/El-Wumbus/qa/releases/latest>`__ for your
platform. These are standalone, portable binary releases with the python
interpreter and dependencies included in the binary.

From Source (Linux/macOS)
*************************

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
*********************

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