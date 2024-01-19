# BNSF Truncator (for Python 2.7) by Quasi-Detective
# 2021.02.09
# Aims to fix BNSF files exported by NUBExt that have empty bytes at the end and therefore won't play in foobar2000.
# Place this script as a .py file into the folder with BNSF files you want to scan/truncate. Please make backups of the BNSF files if you want to revert any changes or in case there is an issue!

import os
import binascii
import sys

for fileO in os.listdir('.'):
    if fileO.endswith(".bnsf") and os.path.isfile(fileO):
        with open(fileO, "rb+") as f:
            print("File: %s" % str(fileO))
            f.seek(-8, os.SEEK_END)
            bytr = binascii.hexlify(f.readline(8))
            print("File position: %s" % str(f.tell()))
            print("Last 8 bytes of file: %s" % str(bytr))

            if bytr == '0000000000000000':
                print("BNSF file is too long!")
                sizeb = os.path.getsize(fileO)
                print("Full size of file in bytes: %s" % str(sizeb))
                sizeE = sizeb - 8
                print("Size of file - 8 bytes: %s" % str(sizeE))
                f.truncate(sizeE)
                print("BNSF file truncated to proper length.\n")
            else:
                print("BNSF file should work!\n")

            f.close()

try:            
    done = input("Truncation complete. Press any key to exit.")
except EOFError:
    done = "\n"
finally:
    sys.exit()