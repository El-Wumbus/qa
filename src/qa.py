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
    True

def load(dir: str, archive_name: str, mode: str):
    # Check if an archive exists and prompt the user
    archive_exists = os.path.exists(archive_name)
    if archive_exists:
        overwrite = std.uconfirm(
            f"File '{archive_name}' already exists. Overwrite?")
        if not overwrite:
            return(0)
        os.remove(archive_name)

    adir = os.path.abspath(dir)
    fullmetapath = os.path.join(adir, "metafile.qa")
    if os.path.exists(fullmetapath):
        os.remove(fullmetapath)

    # Create and write to the metafile
    metafile = open(fullmetapath, 'w')
    metafilecontents = (os.path.abspath(dir))
    metafile.write(metafilecontents)
    metafile.close()
    stda.makearchive(dir, archive_name, None)  # make archive
    os.remove(os.path.join(os.path.abspath(dir),
              "metafile.qa"))  # remove metafile

def unload(archive_name: str):
    # Find tmp dir
    if platform.system() != 'Windows':
        TEMPDIR = '/tmp'
    else:
        TEMPDIR = os.path.expanduser('~\\AppData\\Local\\Temp')

    # Decompress to tmp dir
    tmp = os.path.join(TEMPDIR, '/qa')
    stda.unarchive(archive_name, tmp)

    # Read metafile
    fullmetapath = os.path.join(tmp, 'metafile.qa')
    metafile = open(fullmetapath, 'r')
    metafilecontents = metafile.readline()
    metafile.close()

    fullpath = tmp + "/*"
    if os.path.exists(os.path.join(fullmetapath)):
        os.remove(os.path.join(fullmetapath))
    for file in glob(fullpath):
        print(file)
        shutil.copy2(file, metafilecontents)

argv = sys.argv
argc = len(sys.argv)

if argv[1] == 'load':
    print(f"{argv[2]} {argv[3]} {argv[4]}")
    load(argv[2], argv[3], argv[4])
    sys.exit(0)

elif argv[1] == 'unload':
    unload(argv[2])
    sys.exit(0)

compression_mode = 'xz'
try:
    opts, args = getopt.getopt(argv, 'i:d:vhC:o:', [
                               "help", "verbose", "compression-type="])
except getopt.GetoptError:
    std.ERR("Getops Error", 2)
for opt, arg in opts:
    if opt == ('-h', "--help"):
        usage(0)
    elif opt in ('-v', "--verbose"):
        verbose = True
    elif opt in ('-C', "--compression-type"):
        compression_mode = arg

