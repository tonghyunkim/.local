# install dnvm
sudo yum install libunwind unzip node npm
sudo apt-get install libunwind unzip node npm
curl -sSL https://raw.githubusercontent.com/aspnet/Home/dev/dnvminstall.sh | DNX_BRANCH=dev sh && source ~/.dnx/dnvm/dnvm.sh
source ~/.dnx/dnvm/dnvm.sh

#on ubuntu to install mono
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
echo "deb http://download.mono-project.com/repo/debian wheezy main" | sudo tee /etc/apt/sources.list.d/mono-xamarin.list
sudo apt-get update

# on ubunto install nodejs latest
sudo apt-get install curl
curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -
sudo apt-get install -y nodejs

# installing mono
# do not install original 'sudo yum install mono-devl' on centos install by epel
sudo rpm --import "http://keyserver.ubuntu.com/pks/lookup?op=get&search=0x3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF"
sudo yum-config-manager --add-repo http://download.mono-project.com/repo/centos/
sudo yum -y install mono-complete

# dnvm upgrade
dnvm upgrade

# installing yoeman and  generator-aspnet
sudo npm install -g yo
sudo npm install -g generator-aspnet

# make project, build project, run project
mkdir tmp
cd tmp
yo
dnu restore
dnu build
dnx run

