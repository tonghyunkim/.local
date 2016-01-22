sudo yum install xmllib2

#####################################################
# get latest cmake
####################################################

# check your cmake version first

cmake --version

git clone https://cmake.org/cmake.git
cd cmake
./bootstrap

# make sure CXX=gcc and CC=cc in your environment variables
gmake
sudo gmake install

cmake --version

######################################################
# get latest clang
######################################################

# do not get source code from git, do get it from svn

# choose last final
svn ls http://llvm.org/svn/llvm-project/llvm/tags | grep RELEASE
svn ls http://llvm.org/svn/llvm-project/llvm/tags/RELEASE_380
svn ls http://llvm.org/svn/llvm-project/llvm/tags/RELEASE_371
cd
svn co http://llvm.org/svn/llvm-project/llvm/tags/RELEASE_371/final llvm_RELEASE_371

cd llvm_RELEASE_371/tools
svn co http://llvm.org/svn/llvm-project/cfe/tags/RELEASE_371/final clang
cd ../projects
svn co http://llvm.org/svn/llvm-project/compiler-rt/tags/RELEASE_371/final compiler-rt
svn co http://llvm.org/svn/llvm-project/libcxx/tags/RELEASE_371/final libcxx
svn co http://llvm.org/svn/llvm-project/libcxxabi/tags/RELEASE_371/final libcxxabi
cd ..
svn update

############################
# 1st round to build libcxx without libcxxabi.
############################

# make build directory
mkdir ~/llvm_RELEASE_371_build
cd ~/llvm_RELEASE_371_build

# Specifying CMAKE_BUILD_TYPE to Release shall generate performance optimized code.
# Please specify the absolute paths to clang and clang++ to CMAKE_C_COMPILER and DCMAKE_CXX_COMPILER,
# because CMake (ver. 2.8.12 - 3.0.x) has a bug ... See http://www.cmake.org/Bug/view.php?id=15156
# The CMAKE_INSTALL_PREFIX changes the install path from the default /usr/local to /usr.
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ ../llvm_RELEASE_371
make
sudo make install 


# clang/clang++ compiled executables seem to not find libc++ in /usr/lib, but /lib64.
# Use symbolic link to solve this problem.
sudo ln -s /usr/lib/libc++.so.1 /lib64

############################
# Build libcxxabi with libc++.
############################

# Get libcxxabi.
svn co http://llvm.org/svn/llvm-project/libcxxabi/trunk libcxxabi
cd libcxxabi
mkdir tmp
cd tmp
# Without -DCMAKE_CXX_FLAGS="-std=c++11", clang++ seems to use c++03, so libcxxabi which seems to be written in C++11 can't be compiled. It could be a CMakeLists.txt bug of libcxxabi.
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DCMAKE_CXX_FLAGS="-std=c++11" -DLIBCXXABI_LIBCXX_INCLUDES=../../libcxx/include ..
sudo make install
cd ../..

############################
# 2nd round to build libcxx with libcxxabi.
############################
cd libcxx
mkdir tmp
cd tmp
# This time, we want to compile libcxx with libcxxabi, so we have to specify LIBCXX_CXX_ABI=libcxxabi and the path to libcxxabi headers, LIBCXX_LIBCXXABI_INCLUDE_PATHS.
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DLIBCXX_CXX_ABI=libcxxabi -DLIBCXX_LIBCXXABI_INCLUDE_PATHS=../../libcxxabi/include ..
sudo make install

############################
# Write a C++ test program.
############################

// t.cpp
#include <iostream>
using namespace std;
int main() {
  cout << "Hello world!" << endl;
}

############################
# Test C++ compilation by clang++.
############################

# -std specifies the C++ standard. -stdlib specifies the C++ library you want to use with clang/clang++. -lc++abi is necessary, because the new LD (linker and loader) on CentOS 7 doesn't allow indirect library linking.
clang++ -std=c++11 -stdlib=libc++ -lc++abi t.cpp
./a.out


######################################################
# Get and Build ChakraCore
######################################################

# swich from GCC to Clang
export CC="$(which clang)"
export CXX="$(which clang)"

git clone https://github.com/Microsoft/ChakraCore.git 
cd ChakraCore 
git branch linux origin/linux
git checkout linux
cmake . 
make


























