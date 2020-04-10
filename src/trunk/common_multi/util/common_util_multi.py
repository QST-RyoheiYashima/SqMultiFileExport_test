# -*- coding: utf-8 -*-

"""
widget操作以外の共通処理を記述する。
以下は記載禁止:
・IDに依存した処理
・モデルに依存した処理
・Productに依存した処理
Author	: QST R.Yashima
"""

def get_step_section( section_desc ):
	"""
	test.startSectionに指定する文字列を取得する。
	"""
	return "%s" % section_desc

def is_eng():
	"""
	言語設定を取得する.
	:rtype:bool
	:return:designerを英語実行している場合はTrue
	"""
	# return LanguageEnum.english == g_run_language
	return False

def index_lang():
	"""
	言語にあわせたINDEXを取得する。tuple/配列の格納位置に使用する。
	"""
	# TODO:基本的に日本語の想定。必要な場合は別途設定処理を検討。
	#      (Designer側で設定する必要があると思われる。)
	return 1 if is_eng() else 0
