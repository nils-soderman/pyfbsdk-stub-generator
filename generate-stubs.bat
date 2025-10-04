@echo off
SETLOCAL

if "%~1"=="" (
    set version=2026
) else (
    set version=%~1
)

cd pyfbsdk-stub-generator

echo Generating stubs for MotionBuilder %version%

echo Installing dependencies...
"C:/Program Files/Autodesk/MotionBuilder %version%/bin/x64/mobupy.exe" -m pip install -r requirements.txt --target=./env
SET PYTHONPATH=%CD%/env;%PYTHONPATH%

echo Generating stubs...
"C:/Program Files/Autodesk/MotionBuilder %version%/bin/x64/mobupy.exe" -m src --cache "../generated-stub-files/motionbuilder-%version%"

ENDLOCAL
