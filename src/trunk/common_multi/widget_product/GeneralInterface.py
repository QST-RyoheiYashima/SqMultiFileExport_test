# -*- coding: utf-8 -*-

g_on_GeneralInterface_Window = ":TMainWindow_TMainWindow"  # Window本体
g_on_GeneralInterface_close_Button = ":TMainWindow.buttonCancel_QPushButton"  # 閉じる Button

# ログメッセージ変換用
g_replace_gon_mss_v.append( ( "g_on_GeneralInterface_", "多目的ファイル出力ツール" ) )

@section( "多目的ファイル出力ツール_閉じる" )
def GeneralInterface_close():
	"""
	閉じるボタンを押下し、閉じる。
	"""
	common_close( g_on_GeneralInterface_close_Button,
				None,
				g_on_GeneralInterface_Window,
				True )
