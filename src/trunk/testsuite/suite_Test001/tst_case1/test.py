# -*- coding: utf-8 -*-

source( findFile( "scripts", "init_multi.py" ) )  # 共通関数読み込み

def main():
	before_test_multi()

	action_click( g_on_GeneralInterface_Window )

	after_test_multi()

"""
TestLog
	TestCase tst_case1 2020/04/08 16:24:03 D:\squish\SqMultiFileExport_test\src\trunk\testsuite\suite_Test001\tst_case1
	Log selector=-l 2020/04/08 16:24:04 D:\squish\SqMultiFileExport_test\src\trunk\common_out\module\trunk\src\common\util\api_wrapper.py:116
	Log DESIGNER_PATH=C:\Program Files\JMAG-Designer18.1 2020/04/08 16:24:04 D:\squish\SqMultiFileExport_test\src\trunk\common_out\module\trunk\src\common\util\api_wrapper.py:116
	Log TestResultRootPath=D:\autotests\result\18.1 2020/04/08 16:24:04 D:\squish\SqMultiFileExport_test\src\trunk\common_out\module\trunk\src\common\util\api_wrapper.py:116
	Log squish_test_data_folder=\\CW011744\00_common\010_test_automation\testdata 2020/04/08 16:24:04 D:\squish\SqMultiFileExport_test\src\trunk\common_out\module\trunk\src\common\util\api_wrapper.py:116

TODO:
	上記ログに出る情報を合わせるor除外
"""
