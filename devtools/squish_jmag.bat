@echo off

cd /d %~d0%~p0
set COMM_BAT=common.bat
call %COMM_BAT% select_license
call %COMM_BAT% select_install_path
call %COMM_BAT% set_env
call %COMM_BAT% set_env_jmag

REM ���ʐݒ���㏑��
REM ----------------------------------------------------------
set global_script="%global_script_common%","%global_script_jmag%","%global_script_jmag_common%"
set TestEstimated=0.05
set FAIL_OCCURRED=0
REM ���O�o�͗}��.1=True(�}������)
set TestSimpleReport=1
REM ----------------------------------------------------------

echo --------------------------------------------------------------------
call %COMM_BAT% env_echo
echo DESIGNER_PATH=%DESIGNER_PATH%
echo --------------------------------------------------------------------

call %COMM_BAT% run_ide

pause
exit /b

:error
echo �s���Ȓl
echo selector=%selector%
echo p_squish=%p_squish%
pause
