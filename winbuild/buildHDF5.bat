SETLOCAL

set HDF5_VERSION=1.8.20

set ARCHIVE_ROOT_NAME=hdf5-%HDF5_VERSION%
set WORKING_DIR=%ROOT_DIR%\%ARCHIVE_ROOT_NAME%

mkdir %WORKING_DIR%
copy %ARCHIVE_DIR%\%ARCHIVE_ROOT_NAME%.tar.gz %ROOT_DIR%

cd %ROOT_DIR%

%ROOT_DIR%\winbuild\7zip\7za.exe e -aoa %ARCHIVE_ROOT_NAME%.tar.gz
if %ERRORLEVEL% NEQ 0 (exit /b %ERRORLEVEL%)
%ROOT_DIR%\winbuild\7zip\7za.exe x -aoa %ARCHIVE_ROOT_NAME%.tar
if %ERRORLEVEL% NEQ 0 (exit /b %ERRORLEVEL%)

cd %ROOT_DIR%
rem del %ROOT_DIR%\hdf5-1.8.20\config\cmake_ext_mod\ConfigureChecks.cmake
rem del %ROOT_DIR%\hdf5-1.8.20\config\cmake_ext_mod\HDF5Tests.c
rem del %ROOT_DIR%\hdf5-1.8.20\src\H5Omtime.c
rem %ROOT_DIR%\winbuild\patch\bin\patch -f -p1 < %ROOT_DIR%\winbuild\hdf5_patch_1.diff
rem %ROOT_DIR%\winbuild\patch\bin\patch -f -p1 < %ROOT_DIR%\winbuild\hdf5_patch_2.diff

cd %WORKING_DIR%

mkdir %BUILD_DIR%\doc\licenses
copy COPYING %BUILD_DIR%\doc\licenses\hdf5

mkdir gafferBuild
cd gafferBuild
del /f CMakeCache.txt

cmake -C ..\config\cmake\cacheinit.cmake -Wno-dev -G "NMake Makefiles" -DCMAKE_BUILD_TYPE=%BUILD_TYPE% -DCMAKE_INSTALL_PREFIX=%BUILD_DIR% -DCMAKE_C_COMPILER_WORKS=1 -DCMAKE_CXX_COMPILER_WORKS=1 -DHDF5_ENABLE_THREADSAFE=ON -DBUILD_SHARED_LIBS=ON -DBUILD_TESTING=OFF -DHDF5_BUILD_EXAMPLES=OFF -DHDF5_BUILD_FORTRAN=OFF -DHDF5_ENABLE_SZIP_SUPPORT=OFF ..
if %ERRORLEVEL% NEQ 0 (exit /b %ERRORLEVEL%)
cmake --build . --config %BUILD_TYPE% --target install -- -j %NUMBER_OF_PROCESSORS%
if %ERRORLEVEL% NEQ 0 (exit /b %ERRORLEVEL%)

ENDLOCAL