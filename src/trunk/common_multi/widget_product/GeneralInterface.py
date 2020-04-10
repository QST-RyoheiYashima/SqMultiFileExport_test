# -*- coding: utf-8 -*-

"""
多目的ファイル出力ツール操作の共通処理を記述する。
多目的ファイル出力ツールのobject nameは本ファイルにのみ記述される。

以下は記載禁止:
・IDに依存した処理
・モデルに依存した処理
Author	: QST R.Yashima
"""

g_on_GeneralInterface_Window = ":TMainWindow_TMainWindow"  # Window本体

# -- 変換形式
g_on_GeneralInterface_ConversionType_ConvertFilesFromJplot_Radio = ":TMainWindow.buttonToNastran_QRadioButton"  # jplotファイルからNastran/CSV/Universalファイルへの変換 Radio
g_on_GeneralInterface_ConversionType_OutputType_StaticAnalysis_Radio = ":TMainWindow.buttonST_QRadioButton"  # 静解析 Radio
g_on_GeneralInterface_ConversionType_OutputType_TransientAnalysis_Radio = ":TMainWindow.buttonTR_QRadioButton"  # 過渡応答解析 Radio
g_on_GeneralInterface_ConversionType_OutputType_FrequencyAnalysis_Radio = ":TMainWindow.buttonFQ_QRadioButton"  # 周波数応答解析 Radio
g_on_GeneralInterface_ConversionType_CsvFileToConvertFilesFromJcf_Radio = ":TMainWindow.buttonToJcf_QRadioButton"  # CSVファイルからjcfファイルへの変換 Radio

# -- 入力結果ファイルリスト
g_on_GeneralInterface_InputResultFiles_Table = ":TMainWindow.tablePlots_QTableWidget"  # Table
g_on_GeneralInterface_InputResultFiles_Add_Button = ":TMainWindow.buttonAdd_QPushButton"  # 追加 Button
g_on_GeneralInterface_InputResultFiles_Edit_Button = ":TMainWindow.buttonEdit_QPushButton"  # 変更 Button
g_on_GeneralInterface_InputResultFiles_Remove_Button = ":TMainWindow.buttonRemove_QPushButton"  # 削除 Button

# -- 出力メッシュモデル
g_on_GeneralInterface_OutputModel_MeshModelUnit_Combobox = ":TMainWindow.fMeshModelUnitCombo_QComboBox"  # 単位 Combobox
g_on_GeneralInterface_OutputModel_FromTheFileSpecified_Radio = ":TMainWindow.buttonSpecified_QRadioButton"  # ファイルから指定する Radio
g_on_GeneralInterface_OutputModel_FromTheFileSpecified_Browse_Button = ":TMainWindow.pushButton_Specified_QPushButton"  # 参照 Button
g_on_GeneralInterface_OutputModel_SelectedFromTheInputResultFile_Radio = ":TMainWindow.buttonReference_QRadioButton"  # 入力結果ファイルから選択する Radio
g_on_GeneralInterface_OutputModel_SelectedFromTheInputResultFile_Files_Combobox = ":TMainWindow.comboReference_QComboBox"  # 結果ファイル Combobox
g_on_GeneralInterface_OutputModel_NumberOfMeshExtended3DModel_Edit = ""  # 3次元モデル拡張時のメッシュ分割数 Edit

# -- マッピングオプション
g_on_GeneralInterface_MappingOption_DecideSearchDistanceAutomatically_Checkbox = ":TMainWindow.fUseAutoSearchDistanceCheck_QCheckBox"  # 探索距離を自動決定する Checkbox
g_on_GeneralInterface_MappingOption_SearchDistance_Edit = ":TMainWindow.fSearchDistanceEdit_QLineEdit"  # 探索距離 Edit
g_on_GeneralInterface_MappingOption_SearchDistance_Unit_Combobox = ":TMainWindow.fSearchDistanceUnitCombo_QComboBox"  # 単位 Combobox

# -- 出力ファイルタイプ
g_on_GeneralInterface_OutputFileType_Combobox = ":frameOutputFileType.fOutputFileTypeCombo_QComboBox"  # 出力ファイルタイプ Combobox
g_on_GeneralInterface_OutputFileType_OutputMeshInformation_Checkbox = ":frameOutputFileType.checkOutputMeshFile_QCheckBox"  # メッシュ情報を出力する Checkbox
g_on_GeneralInterface_OutputFileType_OutputFile_Browse_Button = ":TMainWindow.pushButton_Output_QPushButton"  # 参照 Button

# -- 出力項目プレビュー
g_on_GeneralInterface_OutputItem_Tree = ":TMainWindow.treeOutput_QTreeWidget"  # Tree

# -- 出力時刻間隔(過渡応答解析のみ)
g_on_GeneralInterface_OutputTimeInterval_ReferToTheTimeIntervalFromTheReferenceFile_Radio = ":frameOutputInterval.buttonIntervalFromFile_QRadioButton"  # 既存の入力結果ファイルの時間間隔を参照する Radio
g_on_GeneralInterface_OutputTimeInterval_SpecifiedTimeInterval_TimeInterval_Combobox = ":frameTarget.comboReferenceInterval_QComboBox"  # 時間間隔 Combobox
g_on_GeneralInterface_OutputTimeInterval_TargetStep_AllSteps_Radio = ":frameTarget.buttonAllSteps_QRadioButton"  # 全ステップ Radio
g_on_GeneralInterface_OutputTimeInterval_TargetStep_SpecifiedRange_Radio = ":frameTarget.buttonSpecifiedSteps_QRadioButton"  # 区間指定 Radio
g_on_GeneralInterface_OutputTimeInterval_TargetStep_SpecifiedRange_Start_Edit = ":frameTarget.editStartStep_QLineEdit"  # 開始 Edit
g_on_GeneralInterface_OutputTimeInterval_TargetStep_SpecifiedRange_End_Edit = ":frameTarget.editEndStep_QLineEdit"  # 終了 Edit
g_on_GeneralInterface_OutputTimeInterval_SpecifiedTimeInterval_Radio = ":frameOutputInterval.buttonSpecifiedInterval_QRadioButton"  # 時間間隔を指定する Radio
g_on_GeneralInterface_OutputTimeInterval_OutputTime_Start_Edit = ":frameOutputTime.editStartTime_QLineEdit"  # 開始 Edit
g_on_GeneralInterface_OutputTimeInterval_OutputTime_End_Edit = ":frameOutputTime.editEndTime_QLineEdit"  # 終了 Edit
g_on_GeneralInterface_OutputTimeInterval_OutputTime_NumberOfDivisioins_Edit = ":frameOutputTime.editStepDiv_QLineEdit"  # ステップ分割数 Edit

# -- 出力周波数指定(周波数応答解析のみ)
g_on_GeneralInterface_OutputFrequency_AllFrequency_Radio = ":fOutputFrequencyRangeFrame.fAllFrequencyRadio_QRadioButton"  # 全周波数を出力 Radio
g_on_GeneralInterface_OutputFrequency_SpecifiedHarmonicOrder_Radio = ":fOutputFrequencyRangeFrame.fSpecifiedHarmonicOrderRadio_QRadioButton"  # 次数を指定 Radio
g_on_GeneralInterface_OutputFrequency_SpecifiedHarmonicOrder_UpperLimitOfHarmonicOrder_Edit = ":fOutputFrequencyRangeFrame.fUpperLimitHarmonicEdit_QLineEdit"  # 次数の上限 Edit
g_on_GeneralInterface_OutputFrequency_SpecifiedHarmonicOrder_LowerLimitOfHarmonicOrder_Edit = ":fOutputFrequencyRangeFrame.fLowerLimitHarmonicEdit_QLineEdit"  # 次数の下限 Edit
g_on_GeneralInterface_OutputFrequency_SpecifiedFrequency_Radio = ":fOutputFrequencyRangeFrame.fSpecifiedFrequencyRadio_QRadioButton"  # 周波数を指定 Radio
g_on_GeneralInterface_OutputFrequency_SpecifiedFrequency_UpperLimitOfFrequency_Edit = ":fOutputFrequencyRangeFrame.fUpperLimitHarmonicEdit_QLineEdit"  # 周波数の上限 Edit
g_on_GeneralInterface_OutputFrequency_SpecifiedFrequency_LowerLimitOfFrequency_Edit = ":fOutputFrequencyRangeFrame.fLowerLimitHarmonicEdit_QLineEdit"  # 周波数の下限 Edit

# -- (共通)
g_on_GeneralInterface_PreviewMeshModel_Button = ":TMainWindow.fMeshModelPreviewButton_QPushButton"  # メッシュ確認 Button
g_on_GeneralInterface_Preview_Result_Button = ":TMainWindow.fResultPreviewButton_QPushButton"  # 結果プレビュー Button
g_on_GeneralInterface_SaveSetting_Button = ":TMainWindow.buttonSaveXml_QPushButton"  # 設定保存 Button
g_on_GeneralInterface_OpenSetting_Button = ":TMainWindow.buttonReadXml_QPushButton"  # 設定読み込み Button
g_on_GeneralInterface_Export_Button = ":TMainWindow.buttonOk_QPushButton"  # 出力 Button
g_on_GeneralInterface_Close_Button = ":TMainWindow.buttonCancel_QPushButton"  # 閉じる Button

# -- (Dlg)
g_on_GeneralInterface_ProgressDlg_Dlg = ":多目的ファイル出力ツール_QProgressDialog"  # 生成中Dlg Dlg
g_on_GeneralInterface_CompleteDlg_Dlg = ":正常終了_QMessageBox"  # 正常終了Dlg Dlg
g_on_GeneralInterface_CompleteDlg_OK_Button = ":正常終了.OK_QPushButton"  # 正常終了Dlg OK Button

# -- (出力ファイルタイプ名)
g_oc_GeneralInterface_OutputFileType_Nas_Free = "MSC Nastranファイル(フリーフィールド)"
g_oc_GeneralInterface_OutputFileType_Nas = "MSC Nastranファイル(固定フィールド)"
g_oc_GeneralInterface_OutputFileType_Nx_Free = "NX Nastranファイル(フリーフィールド)"
g_oc_GeneralInterface_OutputFileType_Nx = "NX Nastranファイル(固定フィールド)"
g_oc_GeneralInterface_OutputFileType_Unv = "Universalファイル"
g_oc_GeneralInterface_OutputFileType_Csv = "CSVファイル"

# ログメッセージ変換用
g_replace_gon_mss_v.append( ( "g_on_GeneralInterface_", "多目的ファイル出力ツール" ) )
g_replace_gon_mss_v.append( ( "g_on_GeneralInterface_ConversionType_", "多目的ファイル出力ツールの変換形式Block" ) )
g_replace_gon_mss_v.append( ( "g_on_GeneralInterface_InputResultFiles_", "多目的ファイル出力ツールの入力結果ファイルリストblock" ) )
g_replace_gon_mss_v.append( ( "g_on_GeneralInterface_OutputModel_", "多目的ファイル出力ツールの出力メッシュモデルblock" ) )
g_replace_gon_mss_v.append( ( "g_on_GeneralInterface_MappingOption_", "多目的ファイル出力ツールのマッピングオプションblock" ) )
g_replace_gon_mss_v.append( ( "g_on_GeneralInterface_OutputFileType_", "多目的ファイル出力ツールの出力ファイルblock" ) )
g_replace_gon_mss_v.append( ( "g_on_GeneralInterface_OutputItem_", "多目的ファイル出力ツールの出力項目プレビューblock" ) )
g_replace_gon_mss_v.append( ( "g_on_GeneralInterface_OutputTimeInterval_", "多目的ファイル出力ツールの出力時間間隔block" ) )
g_replace_gon_mss_v.append( ( "g_on_GeneralInterface_OutputFrequency_", "多目的ファイル出力ツールの出力周波数指定block" ) )

# ------------------------------------
# -- beanクラス
# ------------------------------------
class GeneralInterfaceBean( InputBean ):
	"""
	多目的ファイル出力ツールのデータ入力用Bean
	"""
	def __init__( self ):
		InputBean.__init__( self )  # super呼び出し時、新クラススタイルは使用出来ない

		# -- 変換形式
		self.ConversionType_ConvertFilesFromJplot_Radio = None  # jplotファイルからNastran/CSV/Universalファイルへの変換 Radio
		self.ConversionType_OutputType_StaticAnalysis_Radio = None  # 静解析 Radio
		self.ConversionType_OutputType_TransientAnalysis_Radio = None  # 過渡応答解析 Radio
		self.ConversionType_OutputType_FrequencyAnalysis_Radio = None  # 周波数応答解析 Radio
		self.ConversionType_CsvFileToConvertFilesFromJcf_Radio = None  # CSVファイルからjcfファイルへの変換 Radio

		# -- 入力結果ファイルリスト
		self.InputResultFiles_Table = None  # Table

		# -- 出力メッシュモデル
		self.OutputModel_MeshModelUnit_Combobox = None  # 単位 Combobox
		self.OutputModel_FromTheFileSpecified_Radio = None  # ファイルから指定する Radio
		self.OutputModel_SelectedFromTheInputResultFile_Radio = None  # 入力結果ファイルから選択する Radio
		self.OutputModel_SelectedFromTheInputResultFile_Files_Combobox = None  # 結果ファイル Combobox
		self.OutputModel_NumberOfMeshExtended3DModel_Edit = None  # 3次元モデル拡張時のメッシュ分割数 Edit

		# -- マッピングオプション
		self.MappingOption_DecideSearchDistanceAutomatically_Checkbox = None  # 探索距離を自動決定する Checkbox
		self.MappingOption_SearchDistance_Edit = None  # 探索距離 Edit
		self.MappingOption_SearchDistance_Unit_Combobox = None  # 単位 Combobox

		# -- 出力ファイルタイプ
		self.OutputFileType_Combobox = None  # 出力ファイルタイプ Combobox
		self.OutputFileType_OutputMeshInformation_Checkbox = None  # メッシュ情報を出力する Checkbox

		# -- 出力項目プレビュー
		self.OutputItem_Tree = None  # Tree

		# -- 出力時刻間隔(過渡応答解析のみ)
		self.OutputTimeInterval_ReferToTheTimeIntervalFromTheReferenceFile_Radio = None  # 既存の入力結果ファイルの時間間隔を参照する Radio
		self.OutputTimeInterval_SpecifiedTimeInterval_Radio = None  # 時間間隔を指定する Radio
		self.OutputTimeInterval_SpecifiedTimeInterval_TimeInterval_Combobox = None  # 時間間隔 Combobox
		self.OutputTimeInterval_TargetStep_AllSteps_Radio = None  # 全ステップ Radio
		self.OutputTimeInterval_TargetStep_SpecifiedRange_Radio = None  # 区間指定 Radio
		self.OutputTimeInterval_TargetStep_SpecifiedRange_Start_Edit = None  # 開始 Edit
		self.OutputTimeInterval_TargetStep_SpecifiedRange_End_Edit = None  # 終了 Edit

		# -- 出力周波数指定(周波数応答解析のみ)
		self.OutputFrequency_AllFrequency_Radio = None  # 全周波数を出力 Radio
		self.OutputFrequency_SpecifiedHarmonicOrder_Radio = None  # 次数を指定 Radio
		self.OutputFrequency_SpecifiedFrequency_Radio = None  # 周波数を指定 Radio
		self.OutputFrequency_SpecifiedFrequency_UpperLimitOfFrequency_Edit = None  # 周波数の上限 Edit
		self.OutputFrequency_SpecifiedFrequency_LowerLimitOfFrequency_Edit = None  # 周波数の下限 Edit

		self.OutputMeshModelFilePath = None  # 出力メッシュモデル
		self.OutputFilePath = None  # 出力ファイル名
		self.SelectInputResultFilesBean = None  # 入力結果ファイルの選択 Bean

	def get_attr_names_primary_only( self ):
		"""
		属性を処理順に返却
		"""
		attrs = []

		# -- 変換形式
		attrs.append( "ConversionType_ConvertFilesFromJplot_Radio" )  # jplotファイルからNastran/CSV/Universalファイルへの変換 Radio
		attrs.append( "ConversionType_OutputType_StaticAnalysis_Radio" )  # 静解析 Radio
		attrs.append( "ConversionType_OutputType_TransientAnalysis_Radio" )  # 過渡応答解析 Radio
		attrs.append( "ConversionType_OutputType_FrequencyAnalysis_Radio" )  # 周波数応答解析 Radio
		attrs.append( "ConversionType_CsvFileToConvertFilesFromJcf_Radio" )  # CSVファイルからjcfファイルへの変換 Radio

		# -- 出力メッシュモデル
		attrs.append( "OutputModel_FromTheFileSpecified_Radio" )  # ファイルから指定する Radio
		attrs.append( "OutputModel_SelectedFromTheInputResultFile_Radio" )  # 入力結果ファイルから選択する Radio

		# -- マッピングオプション
		attrs.append( "MappingOption_DecideSearchDistanceAutomatically_Checkbox" )  # 探索距離を自動決定する Checkbox

		# -- 出力ファイルタイプ
		attrs.append( "OutputFileType_Combobox" )  # 出力ファイルタイプ Combobox

		# -- 出力時刻間隔(過渡応答解析のみ)
		attrs.append( "OutputTimeInterval_ReferToTheTimeIntervalFromTheReferenceFile_Radio" )  # 既存の入力結果ファイルの時間間隔を参照する Radio
		attrs.append( "OutputTimeInterval_TargetStep_AllSteps_Radio" )  # 全ステップ Radio
		attrs.append( "OutputTimeInterval_TargetStep_SpecifiedRange_Radio" )  # 区間指定 Radio
		attrs.append( "OutputTimeInterval_SpecifiedTimeInterval_Radio" )  # 時間間隔を指定する Radio

		# -- 出力周波数指定(周波数応答解析のみ)
		attrs.append( "OutputFrequency_AllFrequency_Radio" )  # 全周波数を出力 Radio
		attrs.append( "OutputFrequency_SpecifiedHarmonicOrder_Radio" )  # 次数を指定 Radio
		attrs.append( "OutputFrequency_SpecifiedFrequency_Radio" )  # 周波数を指定 Radio

		return attrs

	def get_attr_names_no_widget_only( self ):
		"""
		非widget項目のみ返却する。
		"""
		attrs = []
		attrs.append( "OutputMeshModelFilePath" )
		attrs.append( "OutputFilePath" )
		attrs.append( "SelectInputResultFilesBean" )
		return attrs

# ------------------------------------
# -- 基本関数(共通)
# ------------------------------------
@section( "多目的ファイル出力ツール_設定" )
def GeneralInterface_set( bean ):
	"""
	材料編集画面に値を設定する。
	:param GeneralInterfaceBean bean	: 入力値Bean
	"""
	if bean is None:
		return

	Bean_set_widgets_by_order( bean )

	if not bean.SelectInputResultFilesBean is None:
		# TODO:1件存在すれば編集、無ければ追加。本テストでは1件のみを想定。
		tbl = get_widget( g_on_GeneralInterface_InputResultFiles_Table )
		if tbl.columnCount > 0:
			wd = get_widgetitem( g_on_GeneralInterface_InputResultFiles_Table, "0/0" )
			actionw_click( wd )
			action_click_Button( g_on_GeneralInterface_InputResultFiles_Edit_Button )
		else:
			action_click_Button( g_on_GeneralInterface_InputResultFiles_Add_Button )

		if bean.ConversionType_OutputType_StaticAnalysis_Radio:
			a = 1  # TODO:各set関数を実行
		elif bean.ConversionType_OutputType_TransientAnalysis_Radio:
			a = 1  # TODO:各set関数を実行
		elif bean.ConversionType_OutputType_TransientAnalysis_Radio:
			a = 1  # TODO:各set関数を実行
		else:
			fatalTestCodeError( "テストコード不備" )

@section( "多目的ファイル出力ツール_閉じる" )
def GeneralInterface_close():
	"""
	閉じるボタンを押下し、閉じる。
	"""
	common_close( g_on_GeneralInterface_Close_Button,
				None,
				g_on_GeneralInterface_Window,
				True )

@section( "多目的ファイル出力ツール_比較" )
def GeneralInterface_compare( bean ):
	"""
	画面項目を比較。(func_argsは実装しない。)
	:param GeneralInterfaceBean bean	: 比較用Bean
	"""
	if bean is None:
		return

	Bean_compare_widgets( bean )

	if not bean.SelectInputResultFilesBean is None:
		# TODO:1件存在すれば編集、無ければ追加。本テストでは1件のみを想定。
		tbl = get_widget( g_on_GeneralInterface_InputResultFiles_Table )
		if tbl.columnCount > 0:
			wd = get_widgetitem( g_on_GeneralInterface_InputResultFiles_Table, "0/0" )
			actionw_click( wd )
			action_click_Button( g_on_GeneralInterface_InputResultFiles_Edit_Button )
		else:
			action_click_Button( g_on_GeneralInterface_InputResultFiles_Add_Button )

		if bean.ConversionType_OutputType_StaticAnalysis_Radio:
			a = 1  # TODO:各compare関数を実行
		elif bean.ConversionType_OutputType_TransientAnalysis_Radio:
			a = 1  # TODO:各compare関数を実行
		elif bean.ConversionType_OutputType_TransientAnalysis_Radio:
			a = 1  # TODO:各compare関数を実行
		else:
			fatalTestCodeError( "テストコード不備" )
