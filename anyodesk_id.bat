@echo off
for /f "delims=" %%i in ('"C:\ProgramData\AnyDesk\AnyDesk.exe" --get-id') do set ID=%%i
echo AnyDesk ID is: %ID%
