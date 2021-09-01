cd /d %~dp0
for %%i in (*.png) do (
	ffmpeg -i "%%i" -c:v libwebp -lossless 1 "%%~ni.webp"
	if not errorlevel 1 if exist "%%~ni.webp" del /q "%%i"
)
