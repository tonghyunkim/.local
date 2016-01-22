# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions

export PERL_LOCAL_LIB_ROOT="$PERL_LOCAL_LIB_ROOT:/home/tkim/perl5";
export PERL_MB_OPT="--install_base /home/tkim/perl5";
export PERL_MM_OPT="INSTALL_BASE=/home/tkim/perl5";
export PERL5LIB="/home/tkim/perl5/lib/perl5:$PERL5LIB";
export PATH="/home/tkim/perl5/bin:$PATH";
