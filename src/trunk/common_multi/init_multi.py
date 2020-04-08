# -*- coding: utf-8 -*-

"""
テスト実行に必要な設定を行う。
各テストケースは本Scriptを最初読み込んで下さい。
Author	: QST R.Yashima
"""

import os

global g_test_simple_report
try:
	g_test_simple_report = os.environ.get( "TestSimpleReport" )
	g_test_simple_report = ( "1" == g_test_simple_report )
# 	print_log( "環境変数取得:TestSimpleReport:" + g_test_simple_report ) # ここはutil未読み込み
except:
	g_test_simple_report = False
# 	print_log( "環境変数取得失敗:TestSimpleReport" ) # ここはutil未読み込み

# 共通関数読み込み
source( findFile( "scripts", "init_test.py" ) )
load_script( "init/init_test_multi.py" )
load_script( "init/init_load_script_multi.py" )
