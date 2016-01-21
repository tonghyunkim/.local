#!/bin/bash
for filename in ~/.local/dotfiles/.*; do
  if [ "${#filename}" -lt 2 ]; then
    cp "$filename" ~/
  fi
done
