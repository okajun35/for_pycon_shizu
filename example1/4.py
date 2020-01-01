import PySimpleGUI as sg

#  セクション1 - オプションの設定と標準レイアウト
sg.theme('Dark Blue 3')

frame1 = sg.Frame('住所', [[sg.Text('郵便番号', size=(15, 1))],
                         [sg.InputText(key='-POST-NUM-')],
                         [sg.Text('都道府県', size=(15, 1), )],
                         [sg.InputText(key='-PREFECTURES-')],
                         [sg.Text('住所', size=(15, 1))],
                         [sg.InputText(key='-ADDRESS-')],
                         ],
                  relief=sg.RELIEF_SUNKEN, tooltip='住所をいれてね！')

layout = [
    [sg.Text('Python GUI')],
    [sg.Text('名前', size=(15, 1)), sg.Input(
        default_text='○○〇×××', key='-USER-NAME-')],  # https://pysimplegui.readthedocs.io/en/latest/#text-input-element-inputtext-input-in
    [sg.Text('住所を入れてね', size=(15, 1)), frame1],  # frame1のレイアウトを入れ子にして入れている
    [sg.Text('電話番号', size=(15, 1)), sg.InputText(
        default_text='xxx-xxx-xxx', key='-PHONE-NUM-')],
    [sg.Submit('実行ボタン')]
]

# セクション 2 - ウィンドウの生成
window = sg.Window('住所を入力', layout)

# セクション 3 - イベントループ
while True:
    event, values = window.read()

    if event is None:
        print('exit')
        break

    if event == '実行ボタン':
        print(values)
        show_message = "名前：" + values['-USER-NAME-'] + 'が入力されました。\n'
        show_message += "郵便番号：" + values['-POST-NUM-'] + 'が入力されました。\n'
        show_message += "都道府県：" + values['-PREFECTURES-'] + 'が入力されました。\n'
        show_message += "住所：" + values['-ADDRESS-'] + 'が入力されました。\n'
        show_message += "電話番号：" + values['-PHONE-NUM-'] + "が入力されました。"

        # ポップアップ
        sg.popup(show_message)

# セクション 4 - ウィンドウの破棄と終了
window.close()
