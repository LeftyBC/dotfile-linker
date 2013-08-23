## Synopsis

dotfile-linker is a utility to symlink dotfiles stored in a directory into your home directory.  This allows for you to commit and sync your dotfiles with a revision control system like git.

## Motivation

Colin and Phil work on a lot of servers via the shell, and they enjoy tweaking and improving our dotfiles regularly.  Keeping things in sync with scp is a lot of work, especially with a few hundred hosts.

If you let git (or the dvcs your of preference) handle your dotfiles' commits and you push them to your central repository, having synced dotfiles is much easier.

## Installation
1. git clone git@github.com:pdufault/dotfile-linker.git
2. cd dotfiles-linker
3. mkdir .dotfiles
4. cd .dotfiles
5. touch _vim
6. ../linker.py
> linking file /home/user/src/dotfile-linker/.dotfiles/_vim to /home/user/.vim

## License

The MIT License (MIT)

Copyright (c) 2013 Colin Moller

