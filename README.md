## Synopsis

dotfile-linker is a utility to symlink dotfiles stored in a directory into your home directory.  This allows for you to commit and sync your dotfiles with a revision control system like git.

## Motivation

Colin and Phil work on a lot of servers via the shell, and they enjoy tweaking and improving their dotfiles regularly.  Keeping these files in sync with scp everywhere is a lot of work, especially with a few hundred hosts.

If you let git (or the dvcs your of preference) handle your dotfiles' commits and you push them to your central repository, having synced dotfiles is much easier.

## Requirements
A basic Python install is all you should really need.  Tested mainly with Python 2.7.

## Installation
```
$ git clone git@github.com:LeftyBC/dotfile-linker.git ~/.dotfiles
$ cd ~/.dotfiles
$ mkdir -p contrib/sources
$ touch contrib/sources/_testfile
$ touch contrib/sources/.testfile2
$ python linker.py
* linking file /home/user/dotfile-linker/.dotfiles/_testfile to /home/user/.testfile 
* linking file /home/user/dotfile-linker/.dotfiles/.testfile2 to /home/user/.testfile2
``` 
 
## Notes
You should create a subdirectory "contrib/sources".  We purposefully omit this directory in the repo to give you the opportunity to use ```git submodule``` or a project like [Giternal](https://github.com/patmaddox/giternal) to track them separately from the main linker repo.

If any files already exist in your home directory, they will be backed up before being replaced by symlinks.

## License

The MIT License (MIT)

Copyright (c) 2013 Colin Moller

