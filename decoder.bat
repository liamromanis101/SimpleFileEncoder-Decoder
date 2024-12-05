@echo off

if "%~1"=="" (
    echo Usage: %~nx0 [encoded_file]
    echo Decodes a hex-encoded file back to its original binary format.
    exit /b 1
)

set input=%~1
set output=%~n1_decoded.bin
echo Decoding "%input%"...

certutil -decodehex "%input%" "%output%" >nul
 
if exist "%output%" (
    echo Decoding complete. Original file restored as "%output%"
) else (
    echo Decoding failed. Please check the input file.
)
 

 
