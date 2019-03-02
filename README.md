# pacman-simulator
by Nimaya Kodikara

# Execute pacman.py script

1. Execute pacman.py script through an IDE (i.e. PyCharm) which has a python compiler or interpreter, press 'run' to execute
2. Execute pacman.py script based upon your OS (https://stackoverflow.com/questions/51448782/run-a-python-script-without-the-ide)

Windows

Create a .bat file in which you need there needs to the command to execute your python file.

e.g. c:\python27\python.exe c:\somescript.py %*

MacOS / Linux

Create a .sh file which can be executed from your shell/terminal or by double clicking its sym link. 
Your .sh file will look like

#!/bin/bash
python PATH_TO_YOUR_PYTHON_FILE

Then you must make it executable via running the following in terminal

chmod u+x PATH_TO_.SH_FILE

Alternatively you can create a symbolic link to your python file and make it executable. This symlink will be executable by double click. To create a symlink:

ln -sf PATH_TO_.SH_FILE PATH_OF_SYMLINK

If you put just a name in place of PATH_OF_SYMLINK it will be created in your present directory.
