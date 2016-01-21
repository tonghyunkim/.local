# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi

# User specific environment and startup programs

PATH=$PATH:$HOME/.local/bin:$HOME/bin

export PATH


############### git prompt for bash
# load script
source $HOME/bin/git-completion.bash
source $HOME/bin/git-prompt.sh

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