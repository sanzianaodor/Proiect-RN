@echo off
setlocal
cd /d "%~dp0"
set TF_CPP_MIN_LOG_LEVEL=3
".\venv\Scripts\labview_python.exe" -u ".\src\app\main.py" %1
