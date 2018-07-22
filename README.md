Gaffer Dependencies
===================

This project contains the source code for all the 3rd party libraries required to build [Gaffer](https://github.com/GafferHQ/gaffer). It is intended to help Gaffer developers get up and running as quickly as possible, and secondarily to provide a record of exactly which dependencies were used for each release of Gaffer, and how they were built.

Usage
-----

We provide prebuilt binary [releases](https://github.com/GafferHQ/dependencies/releases), which should be used in conjunction with Gaffer's [build instructions](https://github.com/GafferHQ/gaffer#building).

Building
--------

We strongly recommend using the precompiled binaries as described above, but if you really like building multiple huge software projects, read on!

### Prerequisites

Since the build covers so many different projects, it requires the installation of several common software development tools, most of which should be installed by default on a typical developer machine. They include (but are probably not limited to) :

#### Linux and OS X
- Make
- CMake
- SCons
- libbz2 (and headers)

See https://github.com/GafferHQ/build for a Docker container which contains all necessary prerequisites.
#### Windows
- Microsoft Visual Studio 2017 (Community edition is a free version that is known to work)
- CMake
- Python 2.7.xx
- Jom
  - Available from Qt: https://wiki.qt.io/Jom
  - Ensure the installation directory is included in your PATH 
- Cygwin packages
  - Bison
  - Flex
  - NASM
  - autoconf
  - gawk
  - grep
  - sed
  - __Flex and Bison should not be installed in a path that contains spaces.__ This includes the installer default (C:\\Program Files (x86)\\) Doing so will prevent Open Shading Language from building.
- Perl with Windows-compatible slash directions
  - Strawberry Perl (strawberryperl.com) is an open-source option.
  - __The Perl installed by Cygwin is not suitable.__ It will fail to build OpenSSL correctly, but it is required for autoconf. __You must have Strawberry Perl (or a compatible alternative) in your PATH environment variable before your Cygwin binaries path.__ Otherwise the OpenSSL build will fail when attempting configuration.

### Invoking the build

The build is controlled by several environment variables, which must be set up before running :

- ARNOLD_ROOT : Path to the root of an Arnold installation
- RMAN_ROOT : Path to the root of a 3delight installation

#### Linux and OS X
The build is then initiated using a Python script, which should be run from the root directory of the project :

```
./build.py --buildDir /path/to/build --projects TBB
```

Variants are specified using the `--variant:<Project>` command line arguments :

```
./build.py --buildDir /path/to/build --variants:Python 3
```
#### Windows
The build is then initiated using the "x64 Native Tools Command Prompt" for Visual Studio 2017. This is a special command prompt that sets up all of the environment variables for Visual Studio to find the various tools needed for building. It is installed with Visual Studio and is accessible from the start menu under Visual Studio 2017.

Individual packages and variants are built using the build.py script in the manner as Linux and OS X dependencies.

#### Universal Python Builder
Some packages are built using a common Python script and configuration settings for each package. These are built by calling the build.py script in the "build" directory (for all of Linux, OS X and Windows) and specifying the package to build and the build directory.

For example, to build Boost on Linux and OS X and you would run:
```
./build/build.py --project Boost --buildDir $BUILD_DIR
```
and on Windows :
```
python build/build.py --project Boost --buildDir %BUILD_DIR%
```
A list of projects that have are built using this script is shown if you run
```
./build/build.py
```