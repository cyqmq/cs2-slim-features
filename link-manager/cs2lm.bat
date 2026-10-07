@echo off
rem cs2lm launcher for CS2 slim server (Windows).
rem Runs the bundled cs2-link-manager source (tools\cs2lm\src) with python.
setlocal
set "DIR=%~dp0"

set "PYCMD="
where python >nul 2>&1
if not errorlevel 1 (
  set "PYCMD=python"
) else (
  where py >nul 2>&1
  if not errorlevel 1 (
    set "PYCMD=py -3"
  )
)
if not defined PYCMD (
  echo cs2lm: requires Python 3.11+ on PATH ^(install from python.org or use 'py' launcher^)
  exit /b 1
)

%PYCMD% -c "import sys; sys.exit(0 if sys.version_info >= (3, 11) else 1)" >nul 2>&1
if errorlevel 1 (
  echo cs2lm: requires Python 3.11+
  exit /b 1
)

set "PYTHONPATH=%DIR%tools\cs2lm\src;%PYTHONPATH%"
%PYCMD% -m cs2lm %*
exit /b %errorlevel%