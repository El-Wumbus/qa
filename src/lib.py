from rich import print as printf
import os
import tarfile
from sys import exit
import os.path
import shutil
import errno


class stdfile:

    def copyall(source: str, destination: str):
        """
        If the source is a file, copy it to the destination. If the source is a directory, copy it to
        the destination

        :param source: The directory you want to copy
        :type source: str
        :param destination: The destination directory where the files will be copied to
        :type destination: str
        """
        try:
            shutil.copytree(source, destination)
        except OSError as exc:  # python >2.5
            if exc.errno in (errno.ENOTDIR, errno.EINVAL):
                shutil.copy(source, destination)
        else:
            raise

    def makearchive(path: str, archive_name: str):
        """
        Takes a path to a directory, an archive name, and creates a tar archive
        of the directory with xz compresion

        :param path: The path to the directory you want to archive
        :type path: str
        :param archive_name: The name of the archive you want to create
        :type archive_name: str
        :type compression_mode: str
        """

        # Creating a tarfile object, and then adding the path to the tarfile object.
        with tarfile.open(archive_name, tarmode) as tar:
            tar.add(path, arcname=os.path.basename(path))

    def unarchive(archive_name: str, output_path: str):
        """
        Takes an archive name and an output path, opens the archive, extracts all the files to the output
        path, and closes the archive

        :param archive_name: The name of the archive file you want to extract
        :type archive_name: str
        :param output_path: The path to the directory where you want to extract the files
        :type output_path: str
        """
        # Opening the archive, extracting all the files to the output path, and then closing the archive.
        with closing(tarfile.open(archive_name, f"r:xz")) as archive_name:
            archive.extractall(path=output_path)
        

    def tmpdir(platform: str):
        """
        This function returns the temporary directory for the current operating system
        
        :param platform: The platform you're running on
        :type platform: str
        :return: the TEMPDIR variable.
        """
        
        # Find tmp dir
        if platform != "Windows":
            TEMPDIR = '/tmp'
        else:
            TEMPDIR = os.path.expanduser("~\\AppData\\Local\\Temp")

        return(TEMPDIR)


class io:
    def ERR(message: str, code: int):
        """
        Prints a message and exits the program with a given exit code

        :param message: The message to print to the console
        :type message: str
        :param code: The exit code to exit with
        :type code: int
        """
        if message != None:
            printf(
                f"[bold red]{message} \[[bold yellow]{code}[/bold yellow]][/bold red]")
        else:
            printf("[bold red]An unknown error has occured![/bold red]")

        if code != None:
            exit(code)
        else:
            exit(1)
