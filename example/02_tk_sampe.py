import tkinter
from tkinter import messagebox

#ボタンがクリックされたら実行
def button_click():
    input_name_value = input_name.get()
    input_address_value = input_address.get()
    input_phone_value = input_phone.get()

    show_message = "名前：" + input_name_value + 'が入力されました。\n'
    show_message += "住所：" + input_address_value + 'が入力されました。\n'
    show_message += "電話番号：" + input_phone_value + "が入力されました。"
    print(show_message)

    # 入力内容をポップアップ画面で表示
    messagebox.showinfo("入力内容" ,show_message)

#ウインドウの作成
root = tkinter.Tk()
root.title("Python GUI")
root.geometry("360x120")

# 名前
input_name_label = tkinter.Label(text="名前")
input_name_label.grid(row=1, column=1, padx=10,)

# 入力欄の作成
input_name = tkinter.Entry(width=40)
input_name.grid(row=1, column=2)


# 住所
input_address_label = tkinter.Label(text="住所")
input_address_label.grid(row=2, column=1, padx=10,)

# 住所入力欄の作成
input_address = tkinter.Entry(width=40)
input_address.grid(row=2, column=2)


# 電話番号
input_phone_label = tkinter.Label(text="名前")
input_phone_label.grid(row=3, column=1, padx=10,)

# 電話番号入力欄の作成
input_phone = tkinter.Entry(width=40)
input_phone.grid(row=3, column=2)

#ボタンの作成
button = tkinter.Button(text="実行ボタン",command=button_click)
button.place(x=10, y=80)

#ウインドウの描画
root.mainloop()