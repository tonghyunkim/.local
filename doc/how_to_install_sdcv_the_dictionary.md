cd ~
mkdir  sdcv

# c++11 and CMake version
wget http://sourceforge.net/projects/sdcv/files/sdcv/sdcv-0.5.0-beta2-Source.tar.bz2

tar xvjf filename.tar.bz2

cd sdcv-0.5.0-beta2-source
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ .




wget https://copr-be.cloud.fedoraproject.org/results/blaskovic/centos/epel-7-x86_64/sdcv-0.4.2-14.fc21/sdcv-0.4.2-14.el7.centos.x86_64.rpm
sudo rpm -ivh sdcv-0.4.2-14.el7.centos.x86_64.rpm




# english dictionaries

refer http://abloz.com/huzheng/stardict-dic/dict.org/

```
sudo mkdir -p /usr/share/stardict/dic/

cd ~/tmp
# Webster's Revised Unabridged Dictionary (1913)
wget http://abloz.com/huzheng/stardict-dic/dict.org/stardict-dictd-web1913-2.4.2.tar.bz2
sudo tar -xvjf stardict-dictd-web1913-2.4.2.tar.bz2 -C /usr/share/stardict/dic

# The Collaborative International Dictionary of English
wget http://abloz.com/huzheng/stardict-dic/dict.org/stardict-dictd_www.dict.org_gcide-2.4.2.tar.bz2
sudo tar -xvjf stardict-dictd_www.dict.org_gcide-2.4.2.tar.bz2 -C /usr/share/stardict/dic

# Longman Dictionary of Contemporary English (this is the most)
wget http://abloz.com/huzheng/stardict-dic/dict.org/stardict-longman-2.4.2.tar.bz2
sudo tar -xvjf stardict-longman-2.4.2.tar.bz2 -C /usr/share/stardict/dic

# Merrian Webster 10th dictionary
http://abloz.com/huzheng/stardict-dic/dict.org/stardict-merrianwebster-2.4.2.tar.bz2
sudo tar -xvjf stardict-merrianwebster-2.4.2.tar.bz2 -C /usr/share/stardict/dic

```


#__END__

# or 
# wget http://prdownloads.sourceforge.net/sdcv/sdcv-0.4.2.tar.bz2
# cd sdcv-0.4.2
# ./configure
# ./make
# ./make install


