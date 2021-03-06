# for_pycon_shizu
[Pythonでデスクトップアプリを簡単に作る方法](https://shizuoka.pycon.jp/session/dario_okazaki/)のcfpよう

当日の[スライド](https://speakerdeck.com/okajun35/pythondedesukutotupuapuriwojian-dan-nizuo-rufang-fa)

## example の中身
examle配下にはデモで使ったファイルがあります。
試す際は`99_Python_Script_Launcher.py`を実行するとランチャーが立ち上がるので便利かと思います。
 
- 01_tk_sample.py
- 02_tk_sample.py
- 03_basic.py
- 05_graph_sample.py
- 07_vba_excell_join.py
- 08_asci_img.py
- 99_Python_Script_Launcher.py

### 01_tk_sample.py
tkinterを使ったサンプル。
こちらのコードは以下のサイトのコードを使用しました。
- https://wynn-blog.com/make-gui-application-with-python 

- 実行結果

![sample1](https://github.com/okajun35/for_pycon_shizu/blob/for_screenshot/example/sample_png/01_basic/1.png)

実行ボタンをクリックした結果

![sample2](https://github.com/okajun35/for_pycon_shizu/blob/for_screenshot/example/sample_png/01_basic/2.png)


### 02_tk_sample.py
tkinterを使ったサンプル。

- 実行結果

![sample3](https://github.com/okajun35/for_pycon_shizu/blob/for_screenshot/example/sample_png/01_basic/3.png)

実行ボタンをクリックした結果

![sample4](https://github.com/okajun35/for_pycon_shizu/blob/for_screenshot/example/sample_png/01_basic/4.png)


### 03_basic.py
02_tk_sample.pyをPySimpleGUIを使って書き直したサンプル。

- 実行結果

![sample5](https://github.com/okajun35/for_pycon_shizu/blob/for_screenshot/example/sample_png/01_basic/5.png)

実行ボタンをクリックした結果

![sample6](https://github.com/okajun35/for_pycon_shizu/blob/for_screenshot/example/sample_png/01_basic/6.png)

### 04_graph_sample.py
公式のグラフのサンプル（ https://pysimplegui.trinket.io/demo-programs　のGraph Element）を一つにまとめてボタンで切り替えるようにしたもの

実行結果
![graph_example](https://github.com/okajun35/for_pycon_shizu/blob/for_screenshot/example/sample_png/02_graph/graph_example.jpg)

### 07_vba_excell_join.py
公式の[Visual Basic Mockup](https://pysimplegui.trinket.io/demo-programs#/examples-for-reddit-posts/visual-basic-mockup)を元にレイアウトを追加、機能追加したもの

実行結果
![vba_result](https://github.com/okajun35/for_pycon_shizu/blob/for_screenshot/example/sample_png/03_vba/VBA_result.jpg)

### 08_asci_img.py
公式の[Demo_Img_Viewer](https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Img_Viewer.py)を参考に[アスキーアートを自動生成する 
](https://tat-pytone.hatenablog.com/entry/2020/02/26/202205)にGUIをつけたもの

実行結果
![asci_result](https://github.com/okajun35/for_pycon_shizu/blob/for_screenshot/example/sample_png/04_asci/asci_example.png)


### 99_Python_Script_Launcher.py
公式の[Demo_Script_Launcher.py](https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Script_Launcher.py)を元にPythonファイルを実行、Vscodeで開くようにしたもの

- 実行結果

![sample1](https://github.com/okajun35/for_pycon_shizu/blob/for_screenshot/example/sample_png/99_launcher/2.png)

Pythonファイルを実行した場合
![sample2](https://github.com/okajun35/for_pycon_shizu/blob/for_screenshot/example/sample_png/99_launcher/2.png)


### 公式のサンプルについて
スライドの中で紹介したものは公式の以下のサンプルになります。

#### matplotlibとの連携
https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Matplotlib.py

#### グラフのソートアニメーション
https://pysimplegui.trinket.io/demo-programs#/graph-element/visualizing-sorts 

#### CPUのリアルタイムアニメーション
https://github.com/PySimpleGUI/PySimpleGUI-Rainmeter-CPU-Cores/blob/master/PySimpleGUI_Rainmeter_CPU_Cores.py

#### PySimpleGUI-exemaker
https://github.com/PySimpleGUI/PySimpleGUI/tree/master/exemaker


