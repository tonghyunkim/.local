yum install -y curl-devel expat-devel gettext-devel openssl-devel zlib-devel gcc perl-ExtUtils-MakeMaker
export GIT_VERSION=2.7.0
mkdir /root/git
cd /root/git
wget "https://www.kernel.org/pub/software/scm/git/git-${GIT_VERSION}.tar.gz"
tar xvzf "git-${GIT_VERSION}.tar.gz"
cd git-${GIT_VERSION}
make prefix=/usr/local all
make prefix=/usr/local install
yum remove -y git
git --version # should be GIT_VERSION
