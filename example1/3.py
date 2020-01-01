import PySimpleGUI as sg

sg.theme('Dark Green 6')

layout = [[sg.Text('Please click the button', key='-TEXT-')],
          [sg.Submit(button_text='実行ボタン')]]

# ウィンサイズはsizeに(縦の大きさ,横の大きさ)で記載
# ただし基本は適切にウィンドウサイズをとるのと、大きさをドラッグで変えられるのでsizeを指定する必要がない
window = sg.Window('show input text', layout, size=(200, 100))

# イベントループ
while True:
    event, values = window.read()
    if event is None:
        break
    if event == '実行ボタン':
        update_text = "Button clicked."
        # 表示内容を更新する際はウィジェットに指定されたkeyの値に.update("文字列")を入れることで可能
        window['-TEXT-'].update(update_text)

window.close()
