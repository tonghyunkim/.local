#!/bin/bash
# set -x
for filename in ~/.local/dotfiles/.*; do
  if [ "${#filename}" -gt 2 ]; then
    cp "$filename" ~/
  fi
done

git config --global user.email "crowdy@outlook.com"
git config --global user.name "tonghyun kim"
