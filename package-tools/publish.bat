@REM echo off
REM Publish current build to pip (https://pypi.org)
REM Make sure you run 'package.bat' first!

REM Set current working directory
cd /d %~dp0

REM Start a virtual environment
python -m venv env
call .\env\Scripts\activate.bat

REM Install requirements
pip install twine

twine upload --repository pypi ../dist/*

REM Deactivate
call .\env\Scripts\deactivate.bat

echo Done.

pause