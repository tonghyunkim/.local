
<pre><code>
sudo yum install epel-release
sudo yum install libunwind unzip node npm

curl -sSL https://raw.githubusercontent.com/aspnet/Home/dev/dnvminstall.sh | DNX_BRANCH=dev sh && source ~/.dnx/dnvm/dnvm.sh
source ~/.dnx/dnvm/dnvm.sh

dnvm --help
dnvm upgrade

# do not install original 'sudo yum install mono-devl' on centos install by epel

sudo rpm --import "http://keyserver.ubuntu.com/pks/lookup?op=get&search=0x3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF"
sudo yum-config-manager --add-repo http://download.mono-project.com/repo/centos/
sudo yum -y install mono-complete
# sudo yum install mono-complete
# sudo yum install ca-certificates-mono

which mono
dnvm upgrade -r mono
dnvm upgrade -r coreclr
dnvm install latest -r coreclr
</code></pre>

## yeoman and aspnet generators
sudo npm install -g yo
sudo npm install -g generator-aspnet







```console

# install dnvm
sudo yum install libunwind unzip node npm
curl -sSL https://raw.githubusercontent.com/aspnet/Home/dev/dnvminstall.sh | DNX_BRANCH=dev sh && source ~/.dnx/dnvm/dnvm.sh
source ~/.dnx/dnvm/dnvm.sh

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
```

<iframe width="420" height="315" src="https://www.youtube.com/embed/kc2ChRzR8Gs" frameborder="0" allowfullscreen></iframe>

https://www.youtube.com/watch?v=kc2ChRzR8Gs&feature=youtu.be

[![youtube video](http://img.youtube.com/vi/kc2ChRzR8Gs/0.jpg)](http://www.youtube.com/watch?v=kc2ChRzR8Gs)