@echo off
if "%1" == "h" goto begin
mshta vbscript:createobject("wscript.shell").run("""%~nx0"" h",0)(window.close)&&exit
:begin
REM

Netsh WLAN connect name=DLUT-EDA
python C:\xxx\autologin.py
