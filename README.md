# JJBA-ASB-BNSF-Fixer
A simple truncator script for Python 2.7 that removes excess null data from ASB's BNSF files so that they can be loaded in foobar.

Aims to fix BNSF files exported by NUBExt that have empty bytes at the end and therefore won't play in foobar2000.
Place this script as a .py file into the folder with BNSF files you want to scan/truncate. Please make backups of the BNSF files if you want to revert any changes or in case there is an issue!
