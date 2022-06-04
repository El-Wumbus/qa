from bz2 import compress
import os
import tarfile
import stdfunc as std

def makearchive(path:str, archive_name:str, compression_mode: str):
  if compression_mode == None or compression_mode == "xz":
    tarmode = "w:xz"
  elif compression_mode == "gz":
    tarmode = "w:gz"
  elif compression_mode == "bz2":
    tarmode = "w:bz2"
  else:
    std.ERR(f"Compression type '{compression_mode}' is not supported", 1)

  with tarfile.open(archive_name, tarmode) as tar:
    tar.add(path, arcname=os.path.basename(path))

# with tarfile.open(archive_name, tarmode) as tar_handle:
#     for root, dirs, files in os.walk(path):
#       for file in files:
#         tar_handle.add(os.path.join(root, file))

def unarchive(archive_name:str, output_path:str):
  tar = tarfile.open(archive_name)
  tar.extractall(output_path)
  tar.close()
