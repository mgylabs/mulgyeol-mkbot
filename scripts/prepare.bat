@echo off
setlocal
cd "%~dp0.."
xcopy /I /Y /E package\data src\data
xcopy /I /Y /E package\info src\info
endlocal
