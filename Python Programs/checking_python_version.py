# How can i checking python version ?

import sys
import platform

# this line giving you a full path
print(f"python version is : {sys.version}")

# this line giving you just version of python that used for current project
print(f"python version is : {platform.python_version()}")
# or you can do this :
print(f"python version is : {sys.version.split()[0]}")


# for more information see this link :
# https://stackoverflow.com/questions/1252163/printing-python-version-in-output