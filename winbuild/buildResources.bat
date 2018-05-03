SETLOCAL

set RESOURCES_VERSION=0.28.0.0

mkdir %BUILD_DIR%\resources
xcopy /E /Q /Y %ROOT_DIR%\gafferResources-%RESOURCES_VERSION%\resources\* %BUILD_DIR%\resources
if %ERRORLEVEL% NEQ 0 (exit /b %ERRORLEVEL%)

ENDLOCAL