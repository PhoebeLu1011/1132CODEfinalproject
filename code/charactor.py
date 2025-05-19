import pygame
import os

# 初始化pygame
pygame.init()

# 設定視窗大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("恐龍跳躍遊戲")

# 設定顏色
WHITE = (255, 255, 255)

# 設定恐龍圖片的大小
dino_width = 100
dino_height = 100

# 加載並縮放恐龍圖片（使用charactor(1).png, charactor(2).png, charactor(3).png）
dino_images = [
    pygame.image.load(os.path.join('images', 'charactor1.png')),
    pygame.image.load(os.path.join('images', 'charactor2.png')),
    pygame.image.load(os.path.join('images', 'charactor3.png'))
]

# 縮放圖片
dino_images = [pygame.transform.scale(image, (dino_width, dino_height)) for image in dino_images]

# 設定恐龍的初始位置
dino_x = 100
dino_y = 400
dino_y_velocity = 0  # 恐龍的垂直速度
dino_is_jumping = False  # 跳躍狀態
gravity = 1  # 重力
jump_strength = -15  # 跳躍強度

# 設定動畫更新的速度
frame_rate = 10  # 每10幀更新一次

# 設定遊戲的主迴圈
clock = pygame.time.Clock()
current_frame = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not dino_is_jumping:
                # 按下空白鍵並且目前不在跳躍中
                dino_is_jumping = True
                dino_y_velocity = jump_strength  # 設定跳躍的初始速度
    
    # 讓恐龍在跳躍時進行物理運算
    if dino_is_jumping:
        # 更新 Y 坐標，讓恐龍跳起來
        dino_y += dino_y_velocity
        dino_y_velocity += gravity  # 重力影響，速度會越來越大
        
        # 當恐龍落地時停止跳躍
        if dino_y >= 400:
            dino_y = 400  # 恐龍回到地面
            dino_is_jumping = False  # 停止跳躍
            dino_y_velocity = 0  # 重置速度

    # 填充背景色
    screen.fill(WHITE)
    
    # 顯示恐龍圖片
    screen.blit(dino_images[current_frame], (dino_x, dino_y))
    
    # 更新動畫幀
    current_frame = (current_frame + 1) % len(dino_images)
    
    # 更新畫面
    pygame.display.update()
    
    # 控制遊戲速度
    clock.tick(frame_rate)

# 離開遊戲
pygame.quit()
