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
import stdarc as stda
import os
import stdfunc as std
import sys
import platform
import shutil
from glob import glob
import getopt
from time import sleep
from rich.console import Console
import rich.progress
from rich.prompt import Confirm


console = Console()


def usage():
    True  # coming soon, im too lazy to do it now


def load(archive_dir: str, archive_name: str, mode: str, force=False):
    """
    It creates a file called metafile.qa in the directory that is being archived. It then writes the
    absolute path of the directory to the file. It then makes the archive and removes the metafile.

    :param archive_dir: The directory that is being archived
    :type archive_dir: str
    :param archive_name: The name of the archive
    :type archive_name: str
    :param mode: This is the compression used. Can be 'xz', 'gz', or 'bz2'.
    :type mode: str
    """
    # Checking if the archive exists and if it does, it asks the user if they want to overwrite it. If
    # they do, it removes the archive and then creates a new one.
    archive_exists = os.path.exists(archive_name)
    if archive_exists and not force:
        overwrite = std.uconfirm(
            f"File '{archive_name}' already exists. Overwrite?")
        if not overwrite:
            return(0)
        console.log(f"Removing \"{archive_name}\"")
        os.remove(archive_name)

    absolute_dir = os.path.abspath(archive_dir)
    fullmetapath = os.path.join(absolute_dir, "metafile.qa")
    if os.path.exists(fullmetapath):
        os.remove(fullmetapath)

    # Create and write to the metafile
    # Creating a file called metafile.qa in the directory that is being archived. It then writes the
    # absolute path of the directory to the file. It then makes the archive and removes the metafile.
    metafilecontents = (os.path.abspath(archive_dir))
    metafile = open(fullmetapath, 'w')
    metafile.write(metafilecontents)
    metafile.close()
    stda.makearchive(archive_dir, archive_name, mode)  # make archive
    os.remove(os.path.join(os.path.abspath(archive_dir),
              "metafile.qa"))  # remove metafile


def unload(archive_name: str, force=False):
    """
    It takes an archive file, decompresses it to a temporary directory, reads the metafile.qa file to
    get the path of the directory that was archived, and then copies the files from the temporary
    directory to the directory that was held within the metafile then deletes the metafile.

    :param archive_name: The name of the archive file
    :type archive_name: str
    """
    # Find tmp dir
    if platform.system() != 'Windows':
        TEMPDIR = '/tmp'
    else:
        TEMPDIR = os.path.expanduser('~\\AppData\\Local\\Temp')

    # Decompress to tmp dir
    tmp = os.path.join(TEMPDIR, 'qa')
    stda.unarchive(archive_name, tmp)

    # Reading the metafile.qa file and getting the path of the directory that was archived.
    fullmetapath = os.path.join(tmp, 'metafile.qa')
    with rich.progress.open(fullmetapath, 'r') as metafile:
        metafilecontents = metafile.readline()
    metafile.close()

    # Copying the files from the tmp directory to the directory that was held within the metafile.
    fullpath = tmp + "/*"
    if os.path.exists(os.path.join(fullmetapath)):
        os.remove(os.path.join(fullmetapath))
    for file in glob(fullpath):
        if os.path.exists(os.path.join(metafilecontents, file)):
            if not force:
                if not Confirm.ask(f"File \"{os.path.join(metafilecontents,file)}\" already exists, overwrite?"):
                    continue
        shutil.copy2(file, metafilecontents)


def main():
    """
    It checks if the first argument is load or unload, and if it is, it runs the load or unload
    function.
    """
    console.log("[bold #5865F2][u]Starting...[/u]")

    # Getting the arguments from the command line.
    argv = sys.argv
    argc = len(sys.argv)

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf", ["help", "force"])
        argsc = len(args)
    except getopt.GetoptError as err:
        std.ERR("Getops Error: {err}", 2)

    doforce = False
    for o, a in opts:
        if o in ["-h", "--help"]:
            usage()
        # Checking if the -f or --force flag is used. If it is, it sets the doforce variable to True.
        elif o in ["-f", "--force"]:
            doforce = True
        else:
            assert False, "unhandled option"

    # Checking if the first argument is load or unload. If it is load, it checks if there are at least 4
    # arguments. If there are, it runs the load function. If there are not, it prints an error message.
    if args[0] == 'load':
        if argsc < 4:
            std.ERR("Too few arguments for the load function", 2)
        load(args[1], args[2], args[3], force=doforce)
        sys.exit(0)

    # If the first argument is unload, it checks if there is at least 1 argument. If there is, it runs
    # the unload function. If there is not, it prints an error message.
    elif args[0] == 'unload':
        if argsc < 1:
            std.ERR("Too few arguments for the unload function", 2)
        unload(args[1], force=doforce)
        sys.exit(0)


if __name__ == "__main__":
    main()
