@echo off
mode con cols=113 lines=15 
color 09
echo 正在开启程序
echo.
echo ┌────────────────────────────────────────────────────────────────────────────┐
set/p=  ■<nul
for /L %%i in (1 1 38) do set /p a= ■<nul&ping /n 1 127.0.0.1>nul
echo 100%%
start Game.pyw
echo └────────────────────────────────────────────────────────────────────────────┘
color 0a
echo 开启完毕
pause







