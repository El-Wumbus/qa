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

from bz2 import compress
import os
import tarfile
import stdfunc as std

def makearchive(path:str, archive_name:str, compression_mode: str):
  """
  Takes a path to a directory, an archive name, and a compression mode, and creates a tar archive
  of the directory with the given compression mode
  
  :param path: The path to the directory you want to archive
  :type path: str
  :param archive_name: The name of the archive you want to create
  :type archive_name: str
  :param compression_mode: The compression mode to use. Can be "xz", "gz", or "bz2"
  :type compression_mode: str
  """
  if compression_mode == None or compression_mode == "xz":
    tarmode = "w:xz"
  elif compression_mode == "gz":
    tarmode = "w:gz"
  elif compression_mode == "bz2":
    tarmode = "w:bz2"
  else:
    std.ERR(f"Compression type '{compression_mode}' is not supported", 1)

  # Creating a tarfile object, and then adding the path to the tarfile object.
  with tarfile.open(archive_name, tarmode) as tar:
    tar.add(path, arcname=os.path.basename(path))

def unarchive(archive_name:str, output_path:str):
  """
  Takes an archive name and an output path, opens the archive, extracts all the files to the output
  path, and closes the archive
  
  :param archive_name: The name of the archive file you want to extract
  :type archive_name: str
  :param output_path: The path to the directory where you want to extract the files
  :type output_path: str
  """
  # Opening the archive, extracting all the files to the output path, and then closing the archive.
  tar = tarfile.open(archive_name)
  tar.extractall(output_path)
  tar.close()
