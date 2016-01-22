##########################
# get latest cmake
#########################

# check your cmake version first

cmake --version

git clone https://cmake.org/cmake.git

cd cmake

./bootstrap

# make sure CXX=gcc and CC=cc in your environment variables

gmake

sudo gmake install

cmake --version

###########################
# get latest clang
###########################

svn ls http://llvm.org/svn/llvm-project/llvm/tags | grep RELEASE
svn ls http://llvm.org/svn/llvm-project/llvm/tags/RELEASE_380
svn ls http://llvm.org/svn/llvm-project/llvm/tags/RELEASE_371
cd
mkdir llvm_source
cd llvm_source
svn co http://llvm.org/svn/llvm-project/llvm/tags/RELEASE_371/final llvm_RELEASE_371


cd
git clone https://github.com/llvm-mirror/llvm.git
mkdir llvm_build
cd llvm_build
../llvm/configure
make



# swich from GCC to Clang




export CC="$(which clang)"
export CXX="$(which clang)"

git clone https://github.com/Microsoft/ChakraCore.git 
cd ChakraCore 
git branch linux origin/linux
git checkout linux
cmake . 
make

