#!/bin/bash
set -x
for filename in ~/.local/dotfiles/.*; do
  if [ "${#filename}" -gt 2 ]; then
    cp "$filename" ~/
  fi
done
