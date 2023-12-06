import pyxel

# fLand 地面にいるかを判定するフラグ
# fLand = True 地面にいる ／ fLand = False ジャンプ中
fLand = True

# v:速度（Y方向）／ g:重力加速度（Y方向）
v = 0
g = 1 

Y_GROUND = 100 # 地面のY座標

# ヒヨコの座標
x = 54
y = Y_GROUND


def jump():
    global fLand, v
    if fLand: # 地面にいる時は、
        v = -10 # 初速を与える
        fLand = False # 「ジャンプ中」へフラグを変更

def hiyoko_update():
    global fLand, g, v, y
    if fLand: # 地面にいる時は、
        return # 何も処理せず return

    # ジャンプ処理
    # ヒヨコのY座標を計算 ※プログラムの肝
    v += g
    y += v

    if y > Y_GROUND: # 地面に着いたら
        y = Y_GROUND
        v = 0
        fLand = True

class App:
    def __init__(self):
        pyxel.init(125, 125) # 生成するウィンドウのサイズ
        pyxel.load("assets/piyo.pyxres") # 別ファイルからヒヨコのロード
        pyxel.run(self.update, self.draw) # Pyxelの定型処理

    def update(self):
        if pyxel.btn(pyxel.KEY_SPACE): # スペースキーでジャンプ
            jump()
        hiyoko_update()

    def draw(self):
        pyxel.cls(col=pyxel.COLOR_WHITE) # 背景（白）の描画
        pyxel.line(0, Y_GROUND+16, pyxel.width, Y_GROUND+16, pyxel.COLOR_BROWN) # 地面の描画
        pyxel.blt(x, y, 0, 0, 0, 16, 16, 1) # ヒヨコの描画

App()
