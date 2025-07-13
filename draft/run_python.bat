@echo off
REM Batch file to run Python scripts with Anaconda

REM Try common Anaconda paths
set ANACONDA_PATHS=C:\Users\%USERNAME%\anaconda3\python.exe;C:\ProgramData\Anaconda3\python.exe;C:\Anaconda3\python.exe;C:\Users\%USERNAME%\miniconda3\python.exe

for %%p in (%ANACONDA_PATHS:;= %) do (
    if exist "%%p" (
        echo Found Python at: %%p
        if "%1"=="compile" (
            "%%p" compile.py %2 %3 %4 %5
        ) else if "%1"=="upload" (
            "%%p" upload.py %2 %3 %4 %5
        ) else if "%1"=="ipecmd" (
            ipecmd-wrapper %2 %3 %4 %5
        ) else if "%1"=="xc8" (
            xc8-wrapper %2 %3 %4 %5
        ) else (
            echo Usage: run_python.bat [compile^|upload^|ipecmd^|xc8] [options]
            echo.
            echo Commands:
            echo   compile  - Compile with XC8
            echo   upload   - Upload with default settings
            echo   ipecmd   - Upload with full IPECMD options
            echo   xc8      - Compile with XC8 (alias for compile)
            echo.
            echo Examples:
            echo   run_python.bat compile
            echo   run_python.bat upload
            echo   run_python.bat upload --test-programmer
            echo   run_python.bat ipecmd --help
        )
        goto :EOF
    )
)

echo Error: Anaconda Python not found in common locations
echo Please check your Anaconda installation
pause
