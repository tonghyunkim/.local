#!/bin/bash

export PS4='+xtrace $LINENO: '
# set -x

declare  -a conf_files=('.tmux.conf')

for filename in ~/.*; do
  if [ -f "$filename" -a "${#filename}" -gt 2 -a -e ~/.local/dotfiles/"$(basename $filename)" ]; then
    echo "saving $filename to ~/.local/dotfiles/";
    cp "$filename" ~/.local/dotfiles/
  fi
done

# delete .viminfo
if [ -e ~/.local/dotfiles/.viminfo ]; then
  rm ~/.local/dotfiles/.viminfo
fi

