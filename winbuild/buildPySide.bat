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

move /Y %BUILD_DIR%\site-packages\PySide2 %BUILD_DIR%\lib64\site-packages\PySide2
move /Y %BUILD_DIR%\site-packages\PySide2-5.6-py2.7.egg-info %BUILD_DIR%\lib64\site-packages\PySide2-5.6-py2.7.egg-info
move /Y %BUILD_DIR%\site-packages\pyside2uic %BUILD_DIR%\lib64\site-packages\pyside2uic

ENDLOCAL