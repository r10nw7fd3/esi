init python:
  import os, zipfile

  copyfrom = "/storage/emulated/0/Download/esmod.zip"
  extractto = "/storage/emulated/0/Android/data/su.sovietgames.everlasting_summer/files"

  if os.path.exists(copyfrom) and os.path.exists(extractto):
    f = open(copyfrom, "r")
    z = zipfile.ZipFile(f)
    z.extractall(extractto)
    z.close()
    f.close()
    os.remove(copyfrom)