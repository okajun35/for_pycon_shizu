#!/usr/bin/env python
import PySimpleGUI as sg
from PIL import Image, ImageTk
import io
import os

import asci_art_transform as asci

"""
参考URL；　https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Img_Viewer.py
"""

def get_img_data(f, maxsize=(600, 450), first=False):
    """Generate image data using PIL
    """
    print("open file:", f)
    img = Image.open(f)
    img.thumbnail(maxsize)
    if first:  # tkinter is inactive the first time
        bio = io.BytesIO()
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()
    return ImageTk.PhotoImage(img)


filename = './model.jpg'  # 最初のファイル

image_elem = sg.Image(data=get_img_data(filename, first=True))
filename_display_elem = sg.Text(filename, size=(80, 3))

# 初期表示時はascに変換してなくてもよい
# './model.jpg'　をうわがいてしまってもよい
# asci_image = tranfa_asci('./model.jpg', './test.png', 16)
asci_image = "./test.png"
asc_image_elem = sg.Image(data=get_img_data(asci_image, first=True))

# define layout, show and read the form
col = [image_elem, asc_image_elem]

col_read_file = [sg.InputText('ファイルを選択', key='-INPUT-TEXT-', enable_events=True, ),
                 sg.FileBrowse('ファイルを読み込む', key='-FILE-',
                               file_types=(('jpegファイル', '*.jpg'), ('png', '*.png'),)),
                 sg.Button('変換')]

layout = [col_read_file,
         [sg.Slider(range=(1,64),
          key='-FONT-SIZE-',
          default_value=16,
         orientation='h',
         )], col]

window = sg.Window('アスキーアートに変換してみよう', layout, return_keyboard_events=True,
                   location=(0, 0), use_default_focus=False)

# loop reading the user input and displaying image, filename
i = 0
while True:
    # read the form
    event, values = window.read()
    print(event, values)
    # perform button and keyboard operations
    if event is None:
        break
    elif event == '変換':
        print(values['-INPUT-TEXT-'])
        if os.path.isfile(values['-INPUT-TEXT-']):
            # Animationするには別スレッドにする必要
            sg.popup_animated(sg.DEFAULT_BASE64_LOADING_GIF, message='実行中',text_color='black', background_color='white', time_between_frames=100)
            asci_image = asci.tranfa_asci(values['-INPUT-TEXT-'], "./test.png", int(values['-FONT-SIZE-']))
            sg.popup_animated(image_source=None)
            print('変換終了')
        else:
            error_massage = values['-INPUT-TEXT-'] + ' は存在してません'
            sg.popup('エラー', error_massage)

        asc_image_elem.update(data=get_img_data(asci_image, first=True))
    elif values['-FILE-'] != '':
        print('FilesBrowse')
        if os.path.isfile(values['-INPUT-TEXT-']):
            image_elem.update(data=get_img_data(values['-INPUT-TEXT-'], first=True))

window.close()
