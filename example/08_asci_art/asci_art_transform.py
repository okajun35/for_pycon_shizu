from PIL import Image, ImageDraw, ImageFont

"""
変換のアルゴリズムは以下を仕様
アスキーアートを自動生成する https://tat-pytone.hatenablog.com/entry/2020/02/26/202205
フォントは「こころ明朝体」https://typingart.net/?p=46 を使用
"""

KANJI = '　一右雨円王音下火花貝学気九休玉金空月犬見五口校左三山子四糸字耳七車手十出女小上森人水正生青夕石赤千川先早草足村大男竹中虫町天田土二日入年白八百文木本名目立力林六'
FONT = './Kokoro.otf'

def r_sum_calc(im, x_f, y_f):
    """
    x × y ピクセルのr値の合計を求める関数
    """
    r_sum_f = 0
    for i in range(x_f):
        for j in range(y_f):
            r, g, b = im.getpixel((i, j))
            r_sum_f = r_sum_f + r
    return r_sum_f


def choose_letter(r_ave_norm_list_f, test_r_f):
    """
    画像を置き換える文字を探す関数
    """
    near_check = 256
    near_index_f = 0
    for i in r_ave_norm_list_f:
        diff = abs(test_r_f-i)
        if diff < near_check:
            near_check = diff
            near_index_f = r_ave_norm_list_f.index(i)
    return near_index_f

def caluc_kanjis_pixcel(font_size):
    x = font_size
    y = font_size
    r_ave_list = []
    r_ave_norm_list = []

    font = ImageFont.truetype(FONT, font_size)
    # 描画に使う文字列　スペースと小学校1年生の漢字
    kanjis = KANJI

    # 文字列kanjisのそれぞれの文字の白ピクセル値を求める
    # TODO：関数化、漢字辞退はこの計算自体は起動時の最初の一回のみでもよい
    # dataclassを使えばよい？

    for kanji, counter in zip(kanjis, range(len(kanjis))):
        im = Image.new('RGB', (x, y), (0, 0, 0))  # 下地となるイメージオブジェクトの生成
        draw = ImageDraw.Draw(im)  # drawオブジェクトを生成
        draw.multiline_text((0, 0), kanjis[counter], fill=(255, 255, 255),
                            font=font)  # 1行分の文字列を画像に描画
        r_ave = 0
        r_sum = r_sum_calc(im, x, y)
        for i in range(x):
            for j in range(y):
                r, g, b = im.getpixel((i, j))
                r_sum = r_sum+r
        r_ave = r_sum/(x*y)
        r_ave_list.append(r_ave)
    offset = min(r_ave_list)
    r_range = max(r_ave_list) - offset
    mag = 255/r_range

    # 0～255に規格化する
    for i in r_ave_list:
        i = (i-offset)*mag
        r_ave_norm_list.append(int(i))

    return r_ave_norm_list

def tranfa_asci(input_file, output_file,font_size):
    # TODO:型ヒントを加える　font_size = int
    r_ave_norm_list = caluc_kanjis_pixcel(font_size)
 
    x = font_size
    y = font_size
    # 描画に使う文字列　スペースと小学校1年生の漢字
    kanjis = KANJI

    im_draw = Image.open(input_file)  # アスキーアートに変換する画像の読み出し
    im_draw_gray = im_draw.convert('L')  # グレースケール画像に変換
    x_im_draw_gray, y_im_draw_gray = im_draw_gray.size  # グレースケール画像サイズ取得

    # 画像を1/x,1/yに縮小
    x_resize = x_im_draw_gray//x
    y_resize = y_im_draw_gray//y
    im_draw_gray_resize = im_draw_gray.resize((x_resize, y_resize))

    # 縮小画像の各ピクセルの輝度を取得し割り当てる文字を探して表示
    im2 = Image.new("RGB", (x_im_draw_gray, y_im_draw_gray), "white")

    # Imageインスタンスを作る
    im_asci = ImageDraw.Draw(im2)

    fnt = ImageFont.truetype(FONT, font_size)

    y_pos = 0
    for y_check in range(y_resize):
        text_row = ''
        for x_check in range(x_resize):
            brightness = 255-im_draw_gray_resize.getpixel((x_check, y_check))
            near_index = choose_letter(r_ave_norm_list, brightness) 
            text_row = text_row + kanjis[near_index]
        text_row = text_row + '\n'
        im_asci.text((0, y_pos), text_row, fill=(0, 0, 0), font=fnt)
        y_pos = y_pos + y

    im2.save(output_file)
    return output_file
