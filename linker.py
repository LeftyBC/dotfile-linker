#!/usr/bin/env python

import os

from os.path import expanduser

"""
invadeHomedir()
  ensures a dotfiles backup dir exists
  looks at all files in the cwd prefixed with the character in dotfileprefix
    if there's a collision, move the old file into the backup directory
  symlink the file into your home directory
"""


def invadeHomedir(backupdir, home, dotfileprefix):
    backuppath = os.path.join(home, backupdir)

    # my dotfiles live in a submodule that lives in contrib/sources
    sourcespath = os.path.join(os.getcwd(), 'contrib', 'sources')

    if not os.path.exists(backuppath):
        os.mkdir(os.path.join(home, backupdir))

    for filename in os.listdir(sourcespath):
        if filename[:1] == dotfileprefix or filename[:1] == ".":
        # if it's already a dotfile, don't mangle the name
        # otherwise, sub "." for the dotfileprefix
            realname = ".%s" % filename[1:]
            fullpath = os.path.join(sourcespath, filename)
            targetpath = os.path.join(home, realname)

        if filename == ".git" or filename == ".gitignore":
        # ignore git metadata so we don't make a repo out of the homedir
            continue

        if os.path.islink(targetpath):
            # target path is a symlink, leave it alone
            continue

        if os.path.exists(targetpath):
            print "+ Moving [%s] to backup directory [%s]"  \
                % (realname, backuppath)
            os.rename(targetpath, os.path.join(backuppath, realname))

        filetype = "file"
        if os.path.isdir(fullpath):
            filetype = "directory"

        print '* linking %s %s to %s' % (filetype, fullpath, targetpath)

        os.symlink(fullpath, targetpath)

    print "* Done!"


if __name__ == "__main__":
    home = expanduser("~")
    backupdir = '.dotfiles-backup'
    dotfileprefix = "_"
    invadeHomedir(backupdir, home, dotfileprefix)
