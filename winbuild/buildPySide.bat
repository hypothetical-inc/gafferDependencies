SETLOCAL

cd %ROOT_DIR%\pyside-setup-6d8dee0

set PATH=%BUILD_DIR%\bin;%PATH%
set PYTHONHOME=%BUILD_DIR%
set PYTHONPATH=%BUILD_DIR%\python;%PYTHONPATH%
rem Pyside will grab "version" from the environment if it exists and get
rem confused with the --ignore-git flag, so unset VERSION temporarily
set VERSION=

if %CMAKE_GENERATOR%=="NMake Makefiles JOM" (
    set CMAKE_PATH="C:\CMake\bin\cmake.exe"
) else (
    set CMAKE_PATH="C:\Program Files\CMake\bin\cmake.exe"
)

python setup.py --ignore-git --qmake=%BUILD_DIR%\bin\qmake.exe --openssl=%BUILD_DIR%\lib --cmake=%CMAKE_PATH% install
if %ERRORLEVEL% NEQ 0 (exit /b %ERRORLEVEL%)

rem The install needs fixing
cd %BUILD_DIR%\lib64\site-packages
mkdir PySide2
move /Y %BUILD_DIR%\site-packages\PySide2\examples PySide2\examples
move /Y %BUILD_DIR%\site-packages\PySide2\include PySide2\include
move /Y %BUILD_DIR%\site-packages\PySide2\plugins PySide2\plugins
move /Y %BUILD_DIR%\site-packages\PySide2\scripts PySide2\scripts
move /Y %BUILD_DIR%\site-packages\PySide2\translations PySide2\translations
move /Y %BUILD_DIR%\site-packages\PySide2\pyside2-lupdate.exe PySide2\pyside2-lupdate.exe
move /Y %BUILD_DIR%\site-packages\PySide2\pyside2-rcc.exe PySide2\pyside2-rcc.exe
move /Y %BUILD_DIR%\site-packages\PySide2\pyside2.dll PySide2\pyside2.dll
move /Y %BUILD_DIR%\site-packages\PySide2\pyside2.lib PySide2\pyside2.lib
move /Y %BUILD_DIR%\site-packages\PySide2\shiboken2.dll PySide2\shiboken2.dll
move /Y %BUILD_DIR%\site-packages\PySide2\shiboken2.lib PySide2\shiboken2.lib
move /Y %BUILD_DIR%\site-packages\PySide2\_utils.py PySide2\_utils.py
move /Y %BUILD_DIR%\site-packages\PySide2\_utils.pyc PySide2\_utils.pyc
move /Y %BUILD_DIR%\site-packages\PySide2\_init_.py PySide2\_init_.py
move /Y %BUILD_DIR%\site-packages\PySide2\_init_.pyc PySide2\_init_.pyc
move /Y %BUILD_DIR%\site-packages\PySide2\*.pyd PySide2\*.pyd

move /Y %BUILD_DIR%\site-packages\PySide2-5.6-py2.7.egg-info PySide2-5.6-py2.7.egg-info
move /Y %BUILD_DIR%\site-packages\pyside2uic %pyside2uic

ENDLOCAL