#!/usr/bin/env python

import sys
import os

from os.path import expanduser


"""
invadeHomedir()
  ensures a dotfiles backup dir exists
  looks at all files in the cwd prefixed with the character in dotfileprefix
    if there's a collusion, move the old file into the backup directory
    symlink the file into your home directory
"""


def invadeHomedir(backupdir, home, dotfileprefix):
    backuppath = os.path.join(home, backupdir)

    if not os.path.exists(backuppath):
        os.mkdir(os.path.join(home, backupdir))

    for filename in os.listdir(os.getcwd()):
        if filename[:1] == dotfileprefix:
            realname = ".%s" % filename[1:]
            fullpath = os.path.join(os.getcwd(), filename)
            targetpath = os.path.join(home, realname)

            if os.path.islink(targetpath):
                # target path is a symlink, leave it alone
                continue

            if os.path.exists(targetpath):
                print "+ Moving %s to backup directory %s" % (realname, backuppath)
                os.rename(targetpath, os.path.join(backuppath, realname))

            if os.path.isdir(fullpath):
                print '* linking directory %s to %s' % (fullpath, targetpath)
            else:
                print '* linking file %s to %s' % (fullpath, targetpath)

            os.symlink(fullpath, targetpath)

if __name__ == "__main__":
    home = expanduser("~")
    backupdir = '.dotfiles-backup'
    dotfileprefix = "_"
    invadeHomedir(backupdir, home, dotfileprefix)
