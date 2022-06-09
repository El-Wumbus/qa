#!/usr/bin/env python3

# qa -- a program that allows for single command compression and extraction an extra feature
#     Copyright (C) 2022  Aidan Neal

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

from posixpath import abspath
import os
from lib import stdfile, io
import sys
import platform
from glob import glob
import getopt
from time import sleep
from rich.console import Console
import rich.progress
from rich.prompt import Confirm
from rich import print as printf
from rich.traceback import install

# Installing the rich.traceback module.
install()


# Creating a console object.
PROGRAM_NAME = "qa"
console = Console()
startingdir = os.path.abspath(".")
hostplatform = platform.system()


def usage():
    """
    It prints out the usage of the program
    """
    printf(
        f"usage:: [bold #5865F2]{PROGRAM_NAME}[/] -- \[[#4E5D94]load[/]|[#7289DA]unload[/]]\
[#4E5D94]target_dir\[load][/] [#7289DA]target-archive.tar.xz\[[#454FBF]both[/]][/]")
    printf(
        f"example:: [bold #5865F2]{PROGRAM_NAME}[/] load \"[bold red]$HOME[/]/.config\" \"./config.tar.xz\"")


def load(archive_dir: str, archive_name: str,force=False):
    """
    It creates a file called metafile.qa in the directory that is being archived. It then writes the
    absolute path of the directory to the file. It then makes the archive and removes the metafile.

    :param archive_dir: The directory that is being archived
    :type archive_dir: str
    :param archive_name: The name of the archive
    :type archive_name: str
    :type mode: str
    """

    # Checking if the host platform is Windows. If it is, it adds a backslash to the end of the
    # archive_dir variable. If it isn't, it adds a forward slash to the end of the archive_dir
    # variable.
    if hostplatform != "Windows":
        if not archive_dir.endswith("/"):
            archive_dir = archive_dir + "/"
    else:
        if not archive_dir.endswith("\\"):
            archive_dir = archive_dir + "\\"

    # Getting the path of the tmp directory.
    TEMPDIR = stdfile.tmpdir(hostplatform)
    tmp = os.path.join(TEMPDIR, 'qa')

    # Checking if the archive exists and if it does, it asks the user if they want to overwrite it. If
    # they do, it removes the archive.
    archive_exists = os.path.exists(archive_name)
    if archive_exists and not force:
        overwrite = Confirm.ask(
            f"File '{archive_name}' already exists. Overwrite?")
        if not overwrite:
            return(0)
        console.log(f"Removing \"{archive_name}\"")
        os.remove(archive_name)

   # Checking if the metafile exists, and if it does, it removes it.
    absolute_dir = os.path.abspath(archive_dir)
    fullmetapath = os.path.join(absolute_dir, "metafile.qa")
    if os.path.exists(fullmetapath):
        os.remove(fullmetapath)

    # Creating a file called metafile.qa in the directory that is being archived. It then writes the
    # absolute path of the directory to the file. It then makes the archive and removes the metafile.
    metafilecontents = (os.path.abspath(archive_dir))
    metafile = open(fullmetapath, 'w')
    metafile.write(metafilecontents)
    metafile.close()
    console.log(
        f"Creating \"{archive_name}\" from \"{archive_dir}\" with {mode} compression")
    stdfile.makearchive(archive_dir, archive_name)  # make archive
    console.log(f"Created \"{archive_dir}\"")
    os.remove(os.path.join(os.path.abspath(archive_dir),
              "metafile.qa"))  # remove metafile


def unload(archive_name: str, force=False):
    """
    It unarchives the archive_name file to a , reads the metafile.qa file 
    to get the path of the directory that was archived, and copies the files
    from the tmp directory to the directory that was held within the metafile
    then deletes the metafile

    :param archive_name: The name of the archive to unload
    :type archive_name: str
    :param force: If set to True, it will overwrite any files that already 
    exists without asking, defaults to False (optional)
    
    """
    
    # Checking if the archive_name is a directory. If it is, it prints an error message.
    if os.path.isdir(archive_name):
        io.ERR(f"\"{archive_name}\" is a directory, not a file!", 1)

    # Find tmp dir
    TEMPDIR = stdfile.tmpdir(platform.system())

    # Decompress to tmp dir
    console.log(f"Extracting \"{archive_name}\"")
    tmp = os.path.join(TEMPDIR, 'qa')
    stdfile.unarchive(archive_name, tmp)
    console.log(f"[#7289DA]Decompressed[/] \"{archive_name}\"")

    # Reading the metafile.qa file and getting the path of the directory that was archived.
    fullmetapath = os.path.join(tmp, 'metafile.qa')
    if not os.path.exists(fullmetapath):
        io.ERR("No metafile found", 1)
    with rich.progress.open(fullmetapath, 'r') as metafile:
        metafilecontents = metafile.readline()
    metafile.close()

    # Copying the files from the tmp directory to the directory that was held within the metafile.
    fullpath = tmp + "/*"
    if os.path.exists(os.path.join(fullmetapath)):
        os.remove(os.path.join(fullmetapath))

    # Checking if the file exists in the directory that was archived. If it does, it asks the user if
    # they want to overwrite it. If they do, it overwrites the file. If they don't, it skips the file.
    for file in glob(fullpath):
        if os.path.exists(os.path.join(metafilecontents, file)):

           # Checking if the file is a directory. If it is, it copies the directory to the directory
           # that was archived without asking to overwrite.
            if os.path.isdir(file):
                stdfile.copyall(file, metafilecontents)
                return

            # Asking the user if they want to overwrite the file. If they do, it overwrites the file.
            # If they don't, it skips the file.
            if not force:
                if not Confirm.ask(f"File \"{os.path.join(metafilecontents, file)}\" already exists, overwrite?"):
                    continue
        stdfile.copyall(file, metafilecontents)
        return


def main():
    """
    It checks if the first argument is load or unload, and if it is, it runs the load or unload
    function.
    """

    # Getting the arguments from the command line.
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf", ["help", "force"])
        argsc = len(args)
    except getopt.GetoptError as err:
        io.ERR("Getops Error: {err}", 2)

    doforce = False
    for o, a in opts:
        if o in ["-h", "--help"]:
            usage()
            return
        # Checking if the -f or --force flag is used. If it is, it sets the doforce variable to True.
        elif o in ["-f", "--force"]:
            doforce = True
        # If the option isn't handled, it prints an error message.
        else:
            assert False, "unhandled option"

    if argsc <= 0:
        io.ERR("Not enough arguments", 2)

    # Checking if the first argument is load or unload. If it is load, it checks if there are at least 4
    # arguments. If there are, it runs the load function. If there are not, it prints an error message.
    if args[0] == 'load':
        if argsc < 3:
            io.ERR("Too few arguments for the load function", 2)
        load(args[1], args[2], force=doforce)
        sys.exit(0)

    # If the first argument is unload, it checks if there is at least 1 argument. If there is, it runs
    # the unload function. If there is not, it prints an error message.
    elif args[0] == 'unload':
        if argsc < 1:
            io.ERR("Too few arguments for the unload function", 2)
        unload(args[1], force=doforce)
        sys.exit(0)


# Checking if the file is being run as a script. If it is, it runs the main function.
if __name__ == "__main__":
    main()
