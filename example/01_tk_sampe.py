# オリジナルコード:https://wynn-blog.com/make-gui-application-with-python 
import tkinter
from tkinter import messagebox

#ボタンがクリックされたら実行
def button_click():
    input_value = input_box.get()
    messagebox.showinfo("クリックイベント",input_value + "が入力されました。")

#ウインドウの作成
root = tkinter.Tk()
root.title("Python GUI")
root.geometry("360x240")

#入力欄の作成
input_box = tkinter.Entry(width=40)
input_box.place(x=10, y=100)

#ラベルの作成
input_label = tkinter.Label(text="ラベル")
input_label.place(x=10, y=70)

#ボタンの作成
button = tkinter.Button(text="実行ボタン",command=button_click)
button.place(x=10, y=130)

#ウインドウの描画
root.mainloop()