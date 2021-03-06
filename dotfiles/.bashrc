# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions

function gitpull () {
  pushd .
  cd ~/.local && git pull && set_files.sh && source ~/.bash_profile
  popd
}

export PERL_LOCAL_LIB_ROOT="$PERL_LOCAL_LIB_ROOT:/home/tkim/perl5";
export PERL_MB_OPT="--install_base /home/tkim/perl5";
export PERL_MM_OPT="INSTALL_BASE=/home/tkim/perl5";
export PERL5LIB="/home/tkim/perl5/lib/perl5:$PERL5LIB";
export PATH="$PATH:$HOME/.local/bin:$HOME/bin:$HOME/perl5/bin:$PATH";

alias ls='ls --color=auto'
alias cdbin='cd ~/.local/bin'
alias cdlocal='cd ~/.local'
alias cddoc='cd ~/.local/doc'
alias cddotfiles='cd ~/.local/dotfiles'
alias httpdconf='less /etc/httpd/conf/httpd.conf'
alias bashrc='vim ~/.bashrc; source ~/.bashrc;'
alias editdoc="vim ~/.local/doc/$(hostname)"
alias gitpush='pushd .; cd ~/.local; git add -A; git commit -m "update document"; git push; popd'
