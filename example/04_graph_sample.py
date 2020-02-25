import PySimpleGUI as sg
from random import randint
import math
"""
以下の公式サンプルを一つに統合しています
https://pysimplegui.trinket.io/demo-programs#/graph-element/graph-element-bar-chart
https://pysimplegui.trinket.io/demo-programs#/graph-element/graph-element-sine-wave
https://pysimplegui.trinket.io/demo-programs#/graph-element/graph-element-line-graph-with-labels
https://pysimplegui.trinket.io/demo-programs#/graph-element/animated-line-graph
"""

# 定数
GRAPH_SIZE = (500, 500)
DATA_SIZE = (500, 500)

#
PLOTS_NUMBER = 30
RAND_MAX = 400

# 折れ線用
LINE_BAR_WIDTH = 10
LINE_BAR_SPACING = 16
LINE_EDGE_OFFSET = 3

# 棒グラフ
BAR_WIDTH = 50
BAR_SPACING = 75
EDGE_OFFSET = 3

# サイングラフ
SIZE_X = GRAPH_SIZE[0]//2
SIZE_Y = GRAPH_SIZE[1]//2
NUMBER_MARKER_FREQUENCY = 25

# アニメ―ション
GRAPH_STEP_SIZE = 5
DELAY = 15  # 時間間隔

# レイアウト
# グラフの描画領域の設定
graph = sg.Graph(GRAPH_SIZE, (0, 0), DATA_SIZE,
                 key='-GRAPH-', background_color='white',)

layout = [[sg.Text('chart demo')],
          [graph],
          [sg.Button('LINE'), sg.Button('chart'), sg.Button('両方'), 
          sg.Button('円グラフ'), sg.Button('サイン波'), sg.Button('アニメーション')]]

window = sg.Window('シンプルなグラフのサンプル', layout)

before_value = 0  # 折れ線グラフの初期化
delay = x = lastx = lasty = 0  # アニメーションの初期化

is_animated = False


def draw_axis():
    """ X軸とY軸に補助線を引く

    グラフエレメントの左下を原点(0,0)と設定しているのを
    グラフ領域の真ん中を原点として移動している
    """

    graph.draw_line((0, SIZE_Y), (SIZE_X*2, SIZE_Y))  # 原点
    graph.draw_line((SIZE_X, 0), (SIZE_X, SIZE_Y*2))

    for x in range(0, SIZE_X*2, NUMBER_MARKER_FREQUENCY):
        graph.draw_line((x, SIZE_Y-3), (x, SIZE_Y+3))  # 目盛りを引く
        if x != 0:
            graph.draw_text(str(x-SIZE_X), (x, SIZE_Y-10),
                            color='green')  # 目盛りの値を引く

    for y in range(0, SIZE_Y*2+1, NUMBER_MARKER_FREQUENCY):
        graph.draw_line((SIZE_X-3, y), (SIZE_X+3, y))
        if y != 0:
            graph.draw_text(str(y-SIZE_Y), (SIZE_X-10, y), color='blue')


while True:

    if is_animated:
        # 定期的に　'__TIMEOUT__' イベントが発行される
        event, values = window.Read(timeout=DELAY)
    else:
        event, values = window.Read()

    if event is None:
        break

    if event == 'LINE':
        is_animated = False
        # ラベル付き折れ線グラフを表示
        graph.Erase()  # グラフの表示両機を削除

        for i in range(PLOTS_NUMBER):
            graph_value = randint(0, 400)
            if i > 0:
                graph.DrawLine(((i-1) * LINE_BAR_SPACING + LINE_EDGE_OFFSET + LINE_BAR_WIDTH/2,  before_value),
                               (i * LINE_BAR_SPACING + LINE_EDGE_OFFSET + LINE_BAR_WIDTH/2, graph_value), color='green', width=1)

            # 折れ線のラベル（yの値）を表示
            graph.DrawText(text=graph_value, location=(
                i * LINE_BAR_SPACING+EDGE_OFFSET+2, graph_value+10))

            graph.DrawPoint((i * LINE_BAR_SPACING + LINE_EDGE_OFFSET +
                             LINE_BAR_WIDTH/2, graph_value), size=3, color='green',)

            before_value = graph_value

    if event == 'chart':
        is_animated = False

        # 棒グラフを削除
        graph.Erase()
        for i in range(PLOTS_NUMBER):
            graph_value = randint(0, 400)
            graph.DrawRectangle(top_left=(i * BAR_SPACING + EDGE_OFFSET, graph_value),
                                bottom_right=(i * BAR_SPACING + EDGE_OFFSET + BAR_WIDTH, 0), fill_color='blue')
            graph.DrawText(text=graph_value, location=(
                i*BAR_SPACING+EDGE_OFFSET+25, graph_value+10))

    if event == '両方':
        is_animated = False

        # 折れ線グラフと棒グラフの両方を表示
        graph.Erase()
        for i in range(PLOTS_NUMBER):
            graph_value = randint(0, 400)
            graph.DrawRectangle(top_left=(i * BAR_SPACING + EDGE_OFFSET, graph_value),
                                bottom_right=(i * BAR_SPACING + EDGE_OFFSET + BAR_WIDTH, 0), fill_color='blue')
            graph.DrawText(text=graph_value, location=(
                i*BAR_SPACING+EDGE_OFFSET+25, graph_value+10))

            if i > 0:
                graph.DrawLine(((i-1) * LINE_BAR_SPACING + LINE_EDGE_OFFSET + LINE_BAR_WIDTH/2,  before_value),
                               (i * LINE_BAR_SPACING + LINE_EDGE_OFFSET + LINE_BAR_WIDTH/2, graph_value), color='green', width=1)

            graph.DrawText(text=graph_value, location=(
                i * LINE_BAR_SPACING+EDGE_OFFSET+2, graph_value+10))

            graph.DrawPoint((i * LINE_BAR_SPACING + LINE_EDGE_OFFSET +
                             LINE_BAR_WIDTH/2, graph_value), size=3, color='green',)
            before_value = graph_value

    if event == '円グラフ':
        is_animated = False
        graph.erase()

        # create_arc()のfillはないので塗りつぶしはできない
        graph.DrawArc(
            (50, 50), (DATA_SIZE[0]-50, DATA_SIZE[1]-50), extent=-200, start_angle=90)
        graph.DrawArc((50, 50), (DATA_SIZE[0]-50, DATA_SIZE[1]-50),
                      extent=-400, start_angle=-110, arc_color="yellow")
        graph.DrawArc((50, 50), (DATA_SIZE[0]-50, DATA_SIZE[1]-50),
                      extent=-50,  start_angle=-510, arc_color="blue")
        graph.DrawArc((50, 50), (DATA_SIZE[0]-50, DATA_SIZE[1]-50),
                      extent=-50,  start_angle=-560, arc_color="red")
        graph.DrawArc((50, 50), (DATA_SIZE[0]-50, DATA_SIZE[1]-50),
                      extent=-20,  start_angle=-610, arc_color="green")

    if event == 'サイン波':
        is_animated = False
        graph.erase()

        draw_axis()
        prev_x = prev_y = None
        for x in range(0, SIZE_X*2):
            y = math.sin(x/75)*100 + SIZE_Y
            if prev_x is not None:
                graph.draw_line((prev_x, prev_y), (x, y), color='red')
            prev_x, prev_y = x, y

    if event == 'アニメーション' or is_animated:

        if not is_animated:
            graph.Erase()  # グラフを一回削除

        is_animated = True

        # 時系列にそって動くグラフを表示
        step_size, delay = GRAPH_STEP_SIZE, DELAY
        y = randint(0, GRAPH_SIZE[1])
        if x < GRAPH_SIZE[0]:  # 　初回
            # window['-GRAPH-'].DrawLine((lastx, lasty), (x, y), width=1)
            graph.DrawLine((lastx, lasty), (x, y), width=1)
        else:
            # window['-GRAPH-'].Move(-step_size, 0)  # グラフ全体を左にずらす
            # window['-GRAPH-'].DrawLine((lastx, lasty), (x, y), width=1)
            graph.Move(-step_size, 0)  # グラフ全体を左にずらす
            graph.DrawLine((lastx, lasty), (x, y), width=1)
            x -= step_size
            lastx, lasty = x, y
        lastx, lasty = x, y
        x += step_size

window.Close()
