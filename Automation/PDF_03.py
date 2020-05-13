# ライブラリを読み込み
import win32com.client
import os
import time

# Excelを起動する
app = win32com.client.Dispatch("Excel.Application")
app.Visible = True
app.DisplayAlerts = False

# PDF化するファイルリストを作成する。
xlsx_list = []
for file in os.listdir():
    base, ext = os.path.splitext(file)
    if ext == '.xlsx':
        xlsx_list.append(file)

# xlsx_listのファイルだけPDFにする。
for pdf_list in xlsx_list:
    # 読み込み元ファイルと書き込み先ディレクトリを指定する
    base_dir = os.path.dirname(__file__)

    input_file = os.path.join(base_dir,pdf_list)
    output_file = os.path.join(base_dir, pdf_list)

    # Excelでワークブックを読み込む
    book = app.Workbooks.Open(input_file)
    # PDF形式で保存
    xlTypePDF = 0
    book.ExportAsFixedFormat(xlTypePDF, output_file)

# Excelを終了
app.Quit()
time.sleep(1)


# xlsx_listのファイルだけPDFにする。
for rm_file in xlsx_list:
    #インプットファイルを削除
    os.remove(rm_file)

# pyファイルを削除する。
print __file__

