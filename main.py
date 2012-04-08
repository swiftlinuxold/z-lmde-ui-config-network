#! /usr/bin/env python

# Check for root user login
import os, sys
if not os.geteuid()==0:
    sys.exit("\nOnly root can run this script\n")

# Get your username (not root)
import pwd
uname=pwd.getpwuid(1000)[0]

# The remastering process uses chroot mode.
# Check to see if this script is operating in chroot mode.
# /home/mint directory only exists in chroot mode
is_chroot = os.path.exists('/home/mint')
dir_develop=''
if (is_chroot):
	dir_develop='/usr/local/bin/develop'
	dir_user = '/home/mint'
else:
	dir_develop='/home/' + uname + '/develop'
	dir_user = '/home/' + uname

# Everything up to this point is common to all Python scripts called by shared-*.sh
# =================================================================================

# THIS IS THE SCRIPT FOR ADDING THE SWIFT LINUX CONFIGURATION SCRIPTS

os.system ('echo ======================================================')
os.system ('echo BEGIN ADDING SWIFT LINUX NETWORK CONFIGURATION SCRIPTS')

import shutil, subprocess

os.system ('echo ADDING ceni')
os.system ('apt-get install -qq ceni')
os.system ('apt-get -f -y install')

os.system ('echo ADDING yad')
os.system ('apt-get install -qq yad')

os.system ('echo ADDING advert-block-antix')
os.system ('apt-get install -qq advert-block-antix')

# Update /etc/hosts file to block ads
src = dir_develop + '/ui-config-network/etc/hosts'
dest = '/etc/hosts'
shutil.copyfile (src, dest)
	
src = dir_develop + '/ui-config-network/usr_local_bin/config-network.py'
dest = '/usr/local/bin/config-network.py'
shutil.copyfile (src, dest)
os.system ('chmod a+rx ' + dest)

src = dir_develop + '/ui-config-network/usr_share_applications/config-network.desktop'
dest = '/usr/share/applications/config-network.desktop'
shutil.copyfile (src, dest)

os.system ('echo FINISHED ADDING NETWORK CONFIGURATION SCRIPTS')
os.system ('echo =============================================')
