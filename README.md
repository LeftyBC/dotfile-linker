## Synopsis

dotfile-linker is a utility to symlink dotfiles stored in a directory into your home directory.  This allows for you to commit and sync your dotfiles with a revision control system like git.

## Motivation

We work on a lot of servers via the shell, and we like tweaking and improving our .bashrc, .vimrc, etc.  Keeping things in sync with scp is a lot of work, especially with a few hundred hosts.

If you let git (or the dvcs your of preference) handle your dotfiles' commits and you push them to your central repository, getting the hosts to sync up is much easier.

## Installation
_Get started_
1. Clone from this github repository
2. cd dotfiles-linker
3. mkdir .dotfiles
4. cd .dotfiles
5. touch _vim
6. ../linker.py
* linking file /home/user/src/dotfile-linker/.dotfiles/_vim to /home/user/.vim

## License

The MIT License (MIT)

Copyright (c) 2013 Colin Moller

