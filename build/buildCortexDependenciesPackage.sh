#!/bin/bash

set -e
shopt -s nullglob

VERSION=0.46.0.0

PYTHON_VERSION=2.7

if [[ `uname` = "Linux" ]] ; then
	SHLIBSUFFIX=".so"
	PLATFORM="linux"
else
	SHLIBSUFFIX=".dylib"
	PLATFORM="osx"
fi

cd $BUILD_DIR

manifest="

	bin/python
	bin/python*[0-9]

	bin/exrheader
	bin/maketx

	lib/libboost_*$SHLIBSUFFIX*
	lib/libboost_test_exec_monitor.a

	lib/libIex*$SHLIBSUFFIX*
	lib/libHalf*$SHLIBSUFFIX*
	lib/libImath*$SHLIBSUFFIX*
	lib/libIlmImf*$SHLIBSUFFIX*
	lib/libIlmThread*$SHLIBSUFFIX*

	lib/libPyIex*$SHLIBSUFFIX*
	lib/libPyImath*$SHLIBSUFFIX*

	lib/libpython*$SHLIBSUFFIX*
	lib/Python.framework*
	lib/python$PYTHON_VERSION

	lib/libtbb*$SHLIBSUFFIX*

	doc/licenses

	python/iexmodule*
	python/imathmodule*

	include/boost
	include/OpenEXR
	include/python*
	include/tbb

"
packageName=cortexDependencies-$VERSION-$PLATFORM
archiveName=$packageName.tar.gz

# Longwinded method for putting a prefix on the filenames
# in the archive - there is an option for this in GNU tar
# but that's not available on OS X.

tar -c -z -f /tmp/intermediate.tar $manifest
rm -rf /tmp/$packageName
mkdir /tmp/$packageName
cd /tmp/$packageName
tar -x -f /tmp/intermediate.tar
cd /tmp
tar -c -z -f `dirname $BUILD_DIR`/$archiveName $packageName
