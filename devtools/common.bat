@echo off
REM  QST作成bat用の共通処理

:init
REM ######################################################################
set diff=%1
set prm2=%2

IF "env_echo"=="%diff%" (
goto :env_echo
)
IF "select_license"=="%diff%" (
goto :select_license
)
IF "select_install_path"=="%diff%" (
goto :select_install_path
)
IF "set_env"=="%diff%" (
goto :set_env
)
IF "set_env_jmag"=="%diff%" (
goto :set_env_jmag
)
IF "set_log_dir_path"=="%diff%" (
goto :set_log_dir_path
)
IF "run_ide"=="%diff%" (
goto :run_ide
)
IF "run"=="%diff%" (
goto :run
)

echo _common.batへの想定外のパラメータ:%diff%
pause
exit /b 0


:env_echo
REM ######################################################################
echo [license]
echo selector=%selector%
echo JSOL_LICENSE_PATH=%JSOL_LICENSE_PATH%
echo flex_license_server_install_dir=%flex_license_server_install_dir%
echo lmx_license_server_install_dir=%lmx_license_server_install_dir%
echo license_dir=%license_file_dir%\%version%
echo [path]
echo SQUISH_PATH=%SQUISH_PATH%
echo TEST_ROOT=%TEST_ROOT%
echo TEST_MODULE_PATH=%TEST_MODULE_PATH%
echo TEST_SUITE_MAIN_PATH=%TEST_SUITE_MAIN_PATH%
echo squish_test_data_folder=%squish_test_data_folder%
echo TestResultRootPath=%TestResultRootPath%
echo [test setting]
echo global_script=%global_script%
echo TestSimpleReport=%TestSimpleReport%
echo TestEstimated=%TestEstimated%
echo TestSaveDesktopImage=%TestSaveDesktopImage%
echo CommonWaitSec=%CommonWaitSec%

exit /b 0


:select_install_path
REM ######################################################################

:select_squish_path
REM squish install path選択
REM ----------------------------------------------------------
REM 設定済みの考慮
REM ****************************************
IF ""=="%SQUISH_PATH%" (
echo.
) ELSE (
echo SQUISH_PATH=%SQUISH_PATH%
goto select_squish_test_path
)

REM 処理本体
set squish1=C:\squish6421_qt511x_msvc14
set squish2=C:\squish6421_qt56x_msvc12
set squish3=C:\squish641_qt56x_msvc12
set squish4=C:\squish641_qt57x_msvc12_win32

echo.
echo 1:%squish1%
echo 2:%squish2%
echo 3:%squish3%

set p_squish=1
set /p p_squish="Enter squish selector value.default %p_squish%:"

if 1==%p_squish% (
set SQUISH_PATH=%squish1%
)
if 2==%p_squish% (
set SQUISH_PATH=%squish2%
)
if 3==%p_squish% (
set SQUISH_PATH=%squish3%
)
REM ****************************************
REM ----------------------------------------------------------

REM SquishTest path選択
REM ----------------------------------------------------------
:select_squish_test_path
REM 設定済みの考慮
REM ****************************************
IF ""=="%TEST_ROOT%" (
echo.
) ELSE (
echo TEST_ROOT=%TEST_ROOT%
goto set_other_path
)

REM 処理本体
set PATH_SquishTest1=D:\squish\SqMultiFileExport_test
set PATH_SquishTest2=D:\squish\TestAutomationBySquish

echo.
echo 1:%PATH_SquishTest1%
echo 2:%PATH_SquishTest2%

set p_PATH_SquishTest=1
set /p p_PATH_SquishTest="Enter SquishTest selector value.default %p_PATH_SquishTest%:"

if 1==%p_PATH_SquishTest% (
set TEST_ROOT=%PATH_SquishTest1%
)
if 2==%p_PATH_SquishTest% (
set TEST_ROOT=%PATH_SquishTest2%
)
REM ****************************************
REM ----------------------------------------------------------

:set_other_path
REM PYTHON
set PYTHON_ROOT_PATH=C:\Python27
set PYTHONPATH=%PYTHON_ROOT_PATH%\Lib\site-packages
set PYTHON_32_BIT_PATH=%PYTHON_ROOT_PATH%\python.exe

REM 結果出力先
set LOG_FOLDER_PATH=C:\log_data\GUI

exit /b 0


:set_env
REM ######################################################################

REM set_install_path後に設定する環境変数

REM module path.branch切り替え時はここのみ修正する
REM 設定済みの考慮
REM ****************************************
IF ""=="%TEST_MODULE_PATH%" (
echo.
) ELSE (
echo TEST_MODULE_PATH=%TEST_MODULE_PATH%
goto set_env_other
)

REM 処理本体
set TEST_MODULE_PATH=%TEST_ROOT%\src\trunk
REM ****************************************

:set_env_other
REM TestSuiteのroot path
set TEST_SUITE_MAIN_PATH=%TEST_MODULE_PATH%\testsuite

REM 固定値
set global_script_common=%TEST_MODULE_PATH%\common_multi
set global_script_jmag=%TEST_MODULE_PATH%\common_out\module\trunk\src\common
set global_script_jmag_common=%TEST_MODULE_PATH%\common_out\module\trunk\src\jmag\common_jmag

REM ログ出力抑制.1=True(抑制あり)
set TestSimpleReport=1
REM 許容誤差率
set TestEstimated=1
REM %TestResultRootPath%\autosave 配下にDesktopイメージを保存する.1=True(保存)
set TestSaveDesktopImage=0
REM 処理全体の待ち時間追加
set CommonWaitSec=1

exit /b 0


:set_env_jmag
REM ######################################################################

REM path
:set_squish_test_data_folder_jmag
REM 設定済みの考慮
REM ****************************************
IF ""=="%squish_test_data_folder%" (
echo.
) ELSE (
echo squish_test_data_folder=%squish_test_data_folder%
goto set_other_path_jmag
)

REM 処理本体
set squish_test_data_folder=\\CW011744\00_common\010_test_automation\testdata
REM ****************************************

REM path
:set_other_path_jmag
set LicGraspTool=C:\99_personal\LicGraspTool_win64_vc12\GraspLicFeature.exe
set flex_license_server_install_dir=C:\JRI\FLEXlm
set lmx_license_server_install_dir=C:\Program Files (x86)\JSOL\LM-X End-user Tools

REM ライセンステストでのみ使用する環境変数
set TestLMX_HOST=localhost
set TestLMX_PORT=6200
set TestLMX_PASSWORD=MyPassword123

REM JMAGでのみ使用する環境変数
set VTB_VERSION=8.0
set LICENSE_FILE_VERSION=18.0

set version=v%LICENSE_FILE_VERSION%
set license_file_dir=autotest_license_files

REM 設定済みの考慮
:set_version_number_jmag
REM ****************************************
IF ""=="%VERSION_NUMBER%" (
echo.
) ELSE (
echo VERSION_NUMBER=%VERSION_NUMBER%
goto AUT_SETTINGS_jmag
)

REM 処理本体
set version_SquishTest1=18.1
set version_SquishTest2=19.0
echo 1:%version_SquishTest1%
echo 2:%version_SquishTest2%

set p_version_SquishTest=1
set /p p_version_SquishTest="Enter SquishTest selector value.default %p_PATH_SquishTest%:"

if 1==%p_version_SquishTest% (
set VERSION_NUMBER=%version_SquishTest1%
)
if 2==%p_version_SquishTest% (
set VERSION_NUMBER=%version_SquishTest2%
)
REM 結果出力先
set TestResultRootPath=D:\autotests\result_multi\%VERSION_NUMBER%
REM ****************************************

REM app
:AUT_SETTINGS_jmag
set DESIGNER_PATH=C:\Program Files\JMAG-Designer%VERSION_NUMBER%

REM AUT_SETTINGS
%SQUISH_PATH%\bin\squishserver --config addAUT "designer" "%DESIGNER_PATH%"
%SQUISH_PATH%\bin\squishserver --config addAUT "GeneralInterface" "%DESIGNER_PATH%"
%SQUISH_PATH%\bin\squishserver --config setAUTTimeout 30

set global_script="%global_script_common%","%global_script_jmag%","%global_script_jmag_common%"

exit /b 0

:set_log_dir_path
REM ######################################################################

set time=%time%

set min=%time:~3,2%
set sec=%time:~6,2%
set hr=%time:~0,2%

REM create a dated filename for the logfile:
REM assumes MM/DD/YYYY format date
@set TODAY=%date%
@set YEAR=%TODAY:~0,4%
@set MONTH=%TODAY:~5,2%
@set DAY=%TODAY:~8,2%

set LOG_FOLDER=%VERSION_NUMBER%x64_%bit%bit_module

REM set log directory
IF "%selector%"=="-f" (
set LOGDIRECTORY=%LOG_FOLDER_PATH%\FLEX\%LOG_FOLDER%\results-%YEAR% %MONTH% %DAY% %hr%.%min%.%sec%
) 

IF "%selector%"=="-l" (
set LOGDIRECTORY=%LOG_FOLDER_PATH%\LMX\%LOG_FOLDER%\results-%YEAR% %MONTH% %DAY% %hr%.%min%.%sec%
) 

IF "%selector%"=="" (
set LOGDIRECTORY=%LOG_FOLDER_PATH%\%LOG_FOLDER%\results-%YEAR% %MONTH% %DAY% %hr%.%min%.%sec%
) 

exit /b 0


:select_license
REM ######################################################################

echo To start license tests please enter the value given below
echo license selector,  flex=-f  LMX=-l

REM 設定済みの考慮
REM ****************************************
IF ""=="%selector%" (
echo.
) ELSE (
echo selector=%selector%
exit /b 0
)

REM 処理本体
set p_license_type=-l
set /p p_license_type="Enter license selector value.-f or -l.default %p_license_type%:"
set selector=%p_license_type%
REM ****************************************

exit /b 0


:run_ide
REM ######################################################################
REM squish ideを起動
%SQUISH_PATH%\bin\squishrunner --config setGlobalScriptDirs %global_script%
%SQUISH_PATH%\squishide.exe

exit /b 0


:run
REM ######################################################################
set TESTSUITE=%prm2%

REM start the squishserver
start "Squishserver Window" /B %SQUISH_PATH%\bin\squishserver --verbose
timeout /t 5 > nul

REM execute the test
echo setGlobalScriptDirs %global_script%
%SQUISH_PATH%\bin\squishrunner --config setGlobalScriptDirs %global_script%

echo --------------------------------------------------------------------
echo TESTSUITE=%TEST_SUITE_MAIN_PATH%\%TESTSUITE%
echo LOGDIRECTORY=%LOGDIRECTORY%
echo %SQUISH_PATH%\bin\squishrunner --testsuite "%TEST_SUITE_MAIN_PATH%\%TESTSUITE%" --reportgen "html,%LOGDIRECTORY%"
echo --------------------------------------------------------------------

%SQUISH_PATH%\bin\squishrunner --testsuite "%TEST_SUITE_MAIN_PATH%\%TESTSUITE%" --reportgen "html,%LOGDIRECTORY%"

REM stop the squishserver
%SQUISH_PATH%\bin\squishserver --stop
timeout /t 5 > nul

exit /b 0
