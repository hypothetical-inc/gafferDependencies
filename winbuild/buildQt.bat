SETLOCAL

cd %ROOT_DIR%\qt-adsk-5.6.1

mkdir %BUILD_DIR%\doc\licenses
copy LICENSE.LGPLv21 %BUILD_DIR%\doc\licenses\qt

rem something upsets the build process for Qt from the build dir
rem so we will path an alternate place for its dependencies
mkdir %BUILD_DIR%\tempqt
mkdir %BUILD_DIR%\tempqt\include
mkdir %BUILD_DIR%\tempqt\lib

copy /Y %BUILD_DIR%\lib\freetype.lib %BUILD_DIR%\tempqt\lib\freetype.lib
copy /Y %BUILD_DIR%\lib\crypto.lib %BUILD_DIR%\tempqt\lib\crypto.lib
copy /Y %BUILD_DIR%\lib\ssl.lib %BUILD_DIR%\tempqt\lib\ssl.lib
copy /Y %BUILD_DIR%\lib\libtiff.lib %BUILD_DIR%\tempqt\lib\libtiff.lib
rem Qt5 wants 'zdll.lib' not 'zlib.lib'
copy %BUILD_DIR%\lib\zlib.lib %BUILD_DIR%\tempqt\lib\zdll.lib
rem Qt5 wants 'libpng.lib' not 'libpng16.lib'
copy %BUILD_DIR%\lib\libpng16.lib %BUILD_DIR%\tempqt\lib\libpng.lib
rem Qt5 wants 'libjpeg.lib' not 'jpeg.lib'
copy %BUILD_DIR%\lib\jpeg.lib %BUILD_DIR%\tempqt\lib\libjpeg.lib

rem freetype and openssl headers
mkdir %BUILD_DIR%\tempqt\include\freetype2
mkdir %BUILD_DIR%\tempqt\include\openssl
xcopy /E /Q /Y %BUILD_DIR%\include\freetype2 %BUILD_DIR%\tempqt\include\freetype2
xcopy /E /Q /Y %BUILD_DIR%\include\openssl %BUILD_DIR%\tempqt\include\openssl

rem zlib headers
copy /Y %BUILD_DIR%\lib\zlib.h %BUILD_DIR%\tempqt\lib\zlib.h
copy /Y %BUILD_DIR%\lib\zconf.h %BUILD_DIR%\tempqt\lib\zconf.h

rem jpeg headers
copy /Y %BUILD_DIR%\lib\jconfig.h %BUILD_DIR%\tempqt\lib\jconfig.h
copy /Y %BUILD_DIR%\lib\jerror.h %BUILD_DIR%\tempqt\lib\jcerror.h
copy /Y %BUILD_DIR%\lib\jmorecfg.h %BUILD_DIR%\tempqt\lib\jmorecfg.h
copy /Y %BUILD_DIR%\lib\jpeglib.h %BUILD_DIR%\tempqt\lib\jpeglib.h

rem tiff headers
copy /Y %BUILD_DIR%\lib\t4.h %BUILD_DIR%\tempqt\lib\t4.h
copy /Y %BUILD_DIR%\lib\tif_config.h %BUILD_DIR%\tempqt\lib\tif_config.h
copy /Y %BUILD_DIR%\lib\tif_config.vc.h %BUILD_DIR%\tempqt\lib\tif_config.vc.h
copy /Y %BUILD_DIR%\lib\tif_config.wince.h %BUILD_DIR%\tempqt\lib\tif_config.wince.h
copy /Y %BUILD_DIR%\lib\tif_dir.h %BUILD_DIR%\tempqt\lib\tif_dir.h
copy /Y %BUILD_DIR%\lib\tif_fax3.h %BUILD_DIR%\tempqt\lib\tif_fax3.h
copy /Y %BUILD_DIR%\lib\tif_predict.h %BUILD_DIR%\tempqt\lib\tif_predict.h
copy /Y %BUILD_DIR%\lib\tiff.h %BUILD_DIR%\tempqt\lib\tiff.h
copy /Y %BUILD_DIR%\lib\tiffconf.h %BUILD_DIR%\tempqt\lib\tiffconf.h
copy /Y %BUILD_DIR%\lib\tiffconf.vc.h %BUILD_DIR%\tempqt\lib\tiffconf.vc.h
copy /Y %BUILD_DIR%\lib\tiffconf.wince.h %BUILD_DIR%\tempqt\lib\tiffconf.wince.h
copy /Y %BUILD_DIR%\lib\tiffio.h %BUILD_DIR%\tempqt\lib\tiffio.h
copy /Y %BUILD_DIR%\lib\tiffiop.h %BUILD_DIR%\tempqt\lib\tiffiop.h
copy /Y %BUILD_DIR%\lib\tiffvers.h %BUILD_DIR%\tempqt\lib\tiffvers.h
copy /Y %BUILD_DIR%\lib\uvcode.h %BUILD_DIR%\tempqt\lib\uvcode.h

rem We need to have the lib dir
set PATH=%PATH%;%BUILD_DIR%\\tempqt\\lib;%BUILD_DIR%\\bin

rem We should probably check this batch file to make sure ERRORLEVEL
rem is set appropriately?

set QMAKESPEC=win32-msvc2015

%ROOT_DIR%\winbuild\jom\jom.exe distclean
call configure.bat -prefix %BUILD_DIR% -plugindir %BUILD_DIR%\qt\plugins -release -opensource -confirm-license -opengl desktop -no-angle -no-audio-backend -no-dbus -skip qtconnectivity -skip qtwebengine -skip qt3d -skip qtdeclarative -skip qtwebkit -nomake examples -nomake tests -system-zlib -no-openssl -I %BUILD_DIR%\tempqt\include -L %BUILD_DIR%\tempqt\lib
if %ERRORLEVEL% NEQ 0 (exit /b %ERRORLEVEL%)

%ROOT_DIR%\winbuild\jom\jom.exe
if %ERRORLEVEL% NEQ 0 (exit /b %ERRORLEVEL%)
%ROOT_DIR%\winbuild\jom\jom.exe install
if %ERRORLEVEL% NEQ 0 (exit /b %ERRORLEVEL%)

ENDLOCAL