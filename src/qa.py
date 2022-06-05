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


def usage():
    True #coming soon, im too lazy to do it now

def load(archive_dir: str, archive_name: str, mode: str):
    """
    It creates a file called metafile.qa in the directory that is being archived. It then writes the
    absolute path of the directory to the file. It then makes the archive and removes the metafile.
    
    :param archive_dir: The directory that is being archived
    :type archive_dir: str
    :param archive_name: The name of the archive
    :type archive_name: str
    :param mode: This is the mode that the program is running in. It can be either "load" or "unload"
    :type mode: str
    :return: the absolute path of the directory that is being archived.
    """
    # Checking if the archive exists and if it does, it asks the user if they want to overwrite it. If
    # they do, it removes the archive and then creates a new one.
    archive_exists = os.path.exists(archive_name)
    if archive_exists:
        overwrite = std.uconfirm(
            f"File '{archive_name}' already exists. Overwrite?")
        if not overwrite:
            return(0)
        os.remove(archive_name)

    absolute_dir = os.path.abspath(archive_dir)
    fullmetapath = os.path.join(absolute_dir, "metafile.qa")
    if os.path.exists(fullmetapath):
        os.remove(fullmetapath)

    # Create and write to the metafile
    # Creating a file called metafile.qa in the directory that is being archived. It then writes the
    # absolute path of the directory to the file. It then makes the archive and removes the metafile.
    metafile = open(fullmetapath, 'w')
    metafilecontents = (os.path.abspath(archive_dir))
    metafile.write(metafilecontents)
    metafile.close()
    stda.makearchive(archive_dir, archive_name, mode)  # make archive
    os.remove(os.path.join(os.path.abspath(archive_dir),
              "metafile.qa"))  # remove metafile

def unload(archive_name: str):
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
    tmp = os.path.join(TEMPDIR, '/qa')
    stda.unarchive(archive_name, tmp)

    # Reading the metafile.qa file and getting the path of the directory that was archived.
    fullmetapath = os.path.join(tmp, 'metafile.qa')
    metafile = open(fullmetapath, 'r')
    metafilecontents = metafile.readline()
    metafile.close()

    # Copying the files from the tmp directory to the directory that was held within the metafile.
    fullpath = tmp + "/*"
    if os.path.exists(os.path.join(fullmetapath)):
        os.remove(os.path.join(fullmetapath))
    for file in glob(fullpath):
        print(file)
        shutil.copy2(file, metafilecontents)

# Getting the arguments from the command line.
argv = sys.argv
argc = len(sys.argv)

# Checking if the first argument is load or unload. If it is load, it will run the load function with
# the second, third, and fourth arguments. If it is unload, it will run the unload function with the
# second argument.
if argv[1] == 'load':
    if argc < 5: ERR("Too few arguments for the load function", 2)
    print(f"{argv[2]} {argv[3]} {argv[4]}")
    load(argv[2], argv[3], argv[4])
    sys.exit(0)

elif argv[1] == 'unload':
    if argc < 3: ERR("Too few arguments for the unload function", 2)
    unload(argv[2])
    sys.exit(0)

try:
    opts, args = getopt.getopt(argv, 'h', [
                               "help"])
except getopt.GetoptError:
    std.ERR("Getops Error", 2)
for opt, arg in opts:
    if opt == ('-h', "--help"):
        usage(0)

