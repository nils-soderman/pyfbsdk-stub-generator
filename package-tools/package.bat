echo off
REM Build a package of the current source files

REM Set current working directory
cd /d %~dp0

REM Start a virtual environment
python -m venv env
call .\env\Scripts\activate.bat

REM Go up one directory
cd ..

REM Install build requirements
pip install build --upgrade

REM Build
python -m build

REM Go up back to the package-tools
cd package-tools

REM Deactivate
call .\env\Scripts\deactivate.bat

echo Done.

pause