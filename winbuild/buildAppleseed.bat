SETLOCAL

set APPLESEED_VERSION=1.8.1-beta

set ARCHIVE_ROOT_NAME=appleseed-%APPLESEED_VERSION%
set WORKING_DIR=%ROOT_DIR%\%ARCHIVE_ROOT_NAME%

mkdir %WORKING_DIR%
copy %ARCHIVE_DIR%\%ARCHIVE_ROOT_NAME%.tar.gz %ROOT_DIR%

cd %ROOT_DIR%

%ROOT_DIR%\winbuild\7zip\7za.exe e -aoa %ARCHIVE_ROOT_NAME%.tar.gz
if %ERRORLEVEL% NEQ 0 (exit /b %ERRORLEVEL%)
%ROOT_DIR%\winbuild\7zip\7za.exe x -aoa %ARCHIVE_ROOT_NAME%.tar
if %ERRORLEVEL% NEQ 0 (exit /b %ERRORLEVEL%)

cd %ROOT_DIR%
%ROOT_DIR%\winbuild\patch\bin\patch -f -p1 < %ROOT_DIR%\winbuild\appleseed_patch_1.diff

cd %WORKING_DIR%

mkdir sandbox\bin
mkdir sandbox\schemas

mkdir build
cd build
del /f CMakeCache.txt

rem We need to have the lib dir
set PATH=%PATH%;%BUILD_DIR%\\lib;%BUILD_DIR%\\bin

rem Appleseed wants LLVMLTO.lib but it's LTO
copy %BUILD_DIR%\lib\LTO.lib %BUILD_DIR%\lib\LLVMLTO.lib

rem Fix for build script
if %CMAKE_GENERATOR%=="NMake Makefiles JOM" (
    copy %ROOT_DIR%\winbuild\win-vs.txt %WORKING_DIR%\cmake\config\win-vs.txt )
if %CMAKE_GENERATOR%=="Ninja" (
    copy %ROOT_DIR%\winbuild\win-vs.txt %WORKING_DIR%\cmake\config\win-vs.txt )

cmake -Wno-dev -G %CMAKE_GENERATOR% -DCMAKE_BUILD_TYPE=%BUILD_TYPE% -DPYTHON_LIBRARY=%BUILD_DIR%\lib\python27.lib -DPYTHON_INCLUDE_DIR=%BUILD_DIR%\include -DWITH_OSL=ON -DWITH_CLI=ON -DWITH_STUDIO=OFF -DWITH_TOOLS=OFF -DWITH_PYTHON=ON -DWITH_OSL=ON -DWITH_TESTS=OFF -DUSE_STATIC_BOOST=OFF -DUSE_STATIC_OIIO=OFF -DUSE_STATIC_EXR=OFF -DUSE_STATIC_OSL=OFF -DUSE_EXTERNAL_ZLIB=ON -DUSE_EXTERNAL_EXR=ON -DUSE_EXTERNAL_PNG=ON -DUSE_EXTERNAL_XERCES=ON -DUSE_EXTERNAL_OSL=ON -DUSE_EXTERNAL_OIIO=ON -DUSE_EXTERNAL_ALEMBIC=ON -DWARNINGS_AS_ERRORS=OFF -DUSE_SSE=ON -DCMAKE_PREFIX_PATH=%BUILD_DIR% -DCMAKE_INSTALL_PREFIX=%BUILD_DIR%\appleseed -DBOOST_ROOT=%BUILD_DIR% -DIMATH_INCLUDE_DIR=%BUILD_DIR%\\include -DIMATH_HALF_LIBRARY=%BUILD_DIR%\\lib\\Half.lib -DIMATH_IEX_LIBRARY=%BUILD_DIR%\\lib\\Iex-2_2.lib -DIMATH_MATH_LIBRARY=%BUILD_DIR%\\lib\\Imath-2_2.lib -DOPENEXR_INCLUDE_DIR=%BUILD_DIR%\\include -DOPENEXR_IMF_LIBRARY=%BUILD_DIR%\\lib\\IlmImf-2_2.lib -DOPENEXR_THREADS_LIBRARY=%BUILD_DIR%\\lib\\IlmThread-2_2.lib -DXERCES_LIBRARY=%BUILD_DIR%\\lib\\xerces-c_3.lib -DOSL_INCLUDE_DIR=%BUILD_DIR%\include -DOSL_EXEC_LIBRARY=%BUILD_DIR%\lib\oslexec.lib -DOSL_COMP_LIBRARY=%BUILD_DIR%\lib\oslcomp.lib -DOSL_QUERY_LIBRARY=%BUILD_DIR%\lib\oslquery.lib -DLLVM_LIBS_DIR=%BUILD_DIR%\lib ..
if %ERRORLEVEL% NEQ 0 (exit /b %ERRORLEVEL%)
cmake --build . --config %BUILD_TYPE% --target install -- -j %NUMBER_OF_PROCESSORS% VERBOSE=1
if %ERRORLEVEL% NEQ 0 (exit /b %ERRORLEVEL%)

ENDLOCAL
