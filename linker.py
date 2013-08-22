#!/usr/bin/env python

import sys
import os

from os.path import expanduser
home = expanduser("~")

backuppath = os.path.join(home,".dotfiles-backup")
if not os.path.exists(backuppath):
	os.mkdir(os.path.join(home,".dotfiles-backup"))

for filename in os.listdir(os.getcwd()):
	if filename[:1] == "_":
		realname = ".%s" % filename[1:]
		fullpath = os.path.join(os.getcwd(),filename)
		targetpath = os.path.join(home,realname)

		if os.path.islink(targetpath):
			# target path is a symlink, leave it alone
			continue

		if os.path.exists(targetpath):
			print "+++ Moving %s to backup directory %s" % (realname, backuppath)
			os.rename(targetpath,os.path.join(backuppath,realname))

		print '*** linking file %s to %s' % (fullpath,targetpath)
		os.symlink(fullpath,targetpath)

