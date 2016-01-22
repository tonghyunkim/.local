cd ~
mkdir  sdcv

# c++11 and CMake version
wget http://sourceforge.net/projects/sdcv/files/sdcv/sdcv-0.5.0-beta2-Source.tar.bz2

tar xvjf filename.tar.bz2

cd sdcv-0.5.0-beta2-source
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ .


#__END__

# or 
# wget http://prdownloads.sourceforge.net/sdcv/sdcv-0.4.2.tar.bz2
# cd sdcv-0.4.2
# ./configure
# ./make
# ./make install


