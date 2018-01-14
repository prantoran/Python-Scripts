import zipfile
import sys
fileName=sys.argv[1]
zipfile = zipfile.ZipFile(fileName, 'r')
zipfile.extractall()
zipfile.close()

