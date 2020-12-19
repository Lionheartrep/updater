#!/usr/bin/python
# This script automates the update/upgrade commands and autoremoves unneeded files

import subprocess
import os

# check if user is root, if not, get root access WIP

# Get update and wait until update has finished downloading
update = subprocess.Popen(['apt-get', 'update'])
update.wait()

# Run the downloaded update
upgrade = subprocess.Popen(['apt-get', 'upgrade', '-y'])
upgrade.wait()

# autoremove packages
remove = subprocess.Popen(['apt-get', 'autoremove', '-y'])
remove.wait()
os.system('echo success')