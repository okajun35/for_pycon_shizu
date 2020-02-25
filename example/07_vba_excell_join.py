# 元のファイル　https://pysimplegui.trinket.io/demo-programs#/examples-for-reddit-posts/visual-basic-mockup

import PySimpleGUI as sg
from os.path import basename

frame1 = [[sg.Radio('1ファイルにシートごとにまとめる', 1, key='-MULTI-SHEET-', default=True)],
          [sg.Radio('1ファイル1シートにまとめる', 1, key='-ONE-SHEET-')]]

col1 = [[sg.Button('実行')],
        [sg.Button('終了')]]


layout = [[sg.Text('ファイル選択', size=(15, 1), justification='right'),
          sg.InputText('ファイル一覧', enable_events=True,),
          sg.FilesBrowse('ファイルを追加', key='-FILES-', file_types=(('Excell ファイル', '*.xlsx'),))],
          [sg.Button('ログをコピー'), sg.Button('ログをクリア')],
          [sg.Output(size=(100, 5), key='-MULTILINE-')],
          [sg.Button('入力一覧をクリア')],
          [sg.Listbox([], size=(100, 10), enable_events=True, key='-LIST-')],
          [sg.Frame('処理内容', frame1), sg.Column(col1)]]

window = sg.Window('エクセルの結合', layout)

new_files = []
new_file_names = []

while True:             # Event Loop
    event, values = window.read()
    if event in (None, '終了'):
        break

    if event == '実行':
        print('処理を実行')
        print('処理対象ファイル：', new_files)

        # ラジオボタンの値によって処理が変わる
        if values['-MULTI-SHEET-']:
            print('複数シートを１ファイルにまとめる')
        elif values['-ONE-SHEET-']:
            print('複数シートを１シートにまとめる')

        # ポップアップ
        sg.popup('処理が正常終了しました')
    elif event == 'ログをクリア':
        print('ログをクリア')
        window.FindElement('-MULTILINE-').Update('')
    elif event == 'ログをコピー':
        window.FindElement('-MULTILINE-').Widget.clipboard_append(window.find_element('-MULTILINE-').Get())
        sg.popup('ログをコピーしました')
    elif event == '入力一覧をクリア':
        print('入力一覧をクリア')

        new_files.clear()
        new_file_names.clear()
        window['-LIST-'].update('')
    elif values['-FILES-'] != '':
        print('FilesBrowse')

        # TODO:実運用には同一ファイルかどうかの処理が必要
        new_files.extend(values['-FILES-'].split(';'))
        new_file_names.extend([basename(file_path) for file_path in new_files])

        print('ファイルを追加')
        window['-LIST-'].update(new_file_names)  # リストボックスに表示します

window.close()
