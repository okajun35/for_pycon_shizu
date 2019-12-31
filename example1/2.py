import PySimpleGUI as sg

sg.theme('Dark Green 6')

layout = [[sg.Text('Please click the button', key='-TEXT-')],
          [sg.Submit(button_text='実行ボタン')]]

# ウィンサイズはsizeに(縦の大きさ,横の大きさ)で記載
window = sg.Window(title='show input text', size=(200, 100)).Layout(layout)

# イベントループ
while True:
    event, values = window.read()
    if event is None:
        break
    if event == '実行ボタン':
        update_text = "Button clicked."
        # 表示内容を更新する際はウィジェットに指定されたkeyの値に.Update("文字列")を入れることで可能
        window.Element('-TEXT-').Update(update_text)

window.close()
