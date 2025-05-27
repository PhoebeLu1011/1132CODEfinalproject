import pygame
import os

# 螢幕設定
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100

# 圖片大小設定
DESIRED_SIZE = (80, 80)
THEME_SIZE = (538, 632)

# 遊戲初始值
INITIAL_STUDY_POINT = 0
INITIAL_ENERGY_POINT = 70
INITIAL_HEALTH_POINT = 70

# 字體設定
FONT_PATH = os.path.join("images/font", "ARCADECLASSIC.TTF")
FONT_CH_PATH = os.path.join("images/font", "NotoSansTC-Black.otf")

# 圖片路徑
IMAGE_PATHS = {
    'RUNNING': [
        os.path.join("images/Dino", "charactor1.png"),
        os.path.join("images/Dino", "charactor2.png"),
        os.path.join("images/Dino", "charactor3.png")
    ],
    'JUMPING': os.path.join("images/Dino", "charactor jump.png"),
    'BG': os.path.join("images/Other", "Chrome Dinosaur Track.png"),
    'STUDY': [
        os.path.join("images/obj", "讀書.png"),
        os.path.join("images/obj", "寫報告.png")
    ],
    'SLEEP': os.path.join("images/obj", "睡覺.png"),
    'DRINK': os.path.join("images/obj", "喝酒.png"),
    'FOOD': os.path.join("images/obj", "食物.png"),
    'TEACHER': os.path.join("images/obj", "教授.png"),
    'CAR': os.path.join("images/obj", "車.png"),
    'TTHEME_GIRL': [
        os.path.join("images/teachertheme", "ttheme_girl_normal.png"),
        os.path.join("images/teachertheme", "ttheme_girl_dunno.png"),
        os.path.join("images/teachertheme", "ttheme_girl_wow.png")
    ],
    'TTHEME_TEACHER': os.path.join("images/teachertheme", "ttheme_teacher.png")
}

# 遊戲設定
GAME_SPEED = 10
HEALTH_DECREASE_INTERVAL = 1000  # 毫秒