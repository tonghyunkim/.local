# .bash_profile

# The main difference with shell config files is that some are only read by "login" shells (eg. when you login from another host, or login at the text console of a local unix machine). these are the ones called, say, .login or .profile or .zlogin (depending on which shell you're using).

# Then you have config files that are read by "interactive" shells (as in, ones connected to a terminal (or pseudo-terminal in the case of, say, a terminal emulator running under a windowing system). these are the ones with names like .bashrc, .tcshrc, .zshrc, etc.

# bash complicates this in that .bashrc is only read by a shell that's both interactive and non-login, so you'll find most people end up telling their .bash_profile to also read .bashrc with something like

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi

# User specific environment and startup programs

PATH=$PATH:$HOME/.local/bin:$HOME/bin

export PATH


############### git prompt for bash
# load script
[[ -r ~/.local/bin/git-completion.bash ]] && \
  source $HOME/.local/bin/git-completion.bash

[[ -r ~/.local/bin/git-prompt.sh ]] && \
  source $HOME/.local/bin/git-prompt.sh

# set prompt variables
GIT_PS1_SHOWDIRTYSTATE=1
GIT_PS1_SHOWUPSTREAM=1
GIT_PS1_SHOWUNTRACKEDFILES=
GIT_PS1_SHOWSTASHSTATE=1

############### prompt variables
# \u user name
# \h host name
# \W working directory
# \w working directory path
# \n new line
# \d date
# \[ beginning of not showing characters
# \] end of not showing characters
# \$ $
export PS1='\[\033[1;32m\]\u\[\033[00m\]:\[\033[1;34m\]\w\[\033[1;31m\]$(__git_ps1)\[\033[00m\] \$ '
##############
