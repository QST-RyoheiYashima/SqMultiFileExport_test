# -*- coding: utf-8 -*-
"""
テストケースサポート関数を定義する。
Author	: QST R.Yashima
"""

def before_test_multi():
	init_test_main()  # 初期設定

	# TODO:テストデータコピー処理等

	startApplication( "GeneralInterface" )

def after_test_multi():
	GeneralInterface_close()
