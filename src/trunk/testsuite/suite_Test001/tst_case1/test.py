# -*- coding: utf-8 -*-

source( findFile( "scripts", "init_multi.py" ) )  # 共通関数読み込み

def main():
	"""
	squishから実行される関数
	"""
	before_test_multi()
	test_step1()
	after_test_multi()

@stepSection( "1" )
def test_step1():
	# 手順1
	action_click( g_on_GeneralInterface_Window )
