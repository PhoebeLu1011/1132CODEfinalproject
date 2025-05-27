import pygame
import random
import os
from constants import *

class GameEvents:
    def __init__(self, screen):
        self.screen = screen
        self.font_ch = pygame.font.Font(FONT_CH_PATH, 24)
        
    def trigger_teacher_event(self, study_point, energy_point):
        run_event = True
        stage = 0
        girl_img = pygame.transform.scale(pygame.image.load(IMAGE_PATHS['TTHEME_GIRL'][0]), THEME_SIZE)
        teacher_img = pygame.transform.scale(pygame.image.load(IMAGE_PATHS['TTHEME_TEACHER']), THEME_SIZE)

        dialogues = [
            ["太好了同學，剛好你來幫我整理這些文件吧", "被迫幫忙教授(精力值-10)", 1, -10, 0],
            ["同學有哪裡不懂嗎", "和教授討論中(讀書進度+10)", 2, 0, 10],
            ["同學你的報告寫得非常好!", "被誇獎了好開心(精力值+5)", 2, +5, 0],
            ["同學你來幫忙紀錄一下這場會議好嗎，還有明天順便幫我聯絡，禮拜五的時候也......", "事情突然好多......(精力值-10，讀書進度-10)", 1, -10, -10],
        ]
        chosen_dialogue = random.choice(dialogues)

        while run_event:
            self.screen.fill((255, 255, 255))
            self.screen.blit(girl_img, (-100, 50))
            self.screen.blit(teacher_img, (650, 20))

            dialogue_text = self.font_ch.render(chosen_dialogue[stage], True, (0, 0, 0))
            self.screen.blit(dialogue_text, (SCREEN_WIDTH // 2 - dialogue_text.get_width() // 2, 150))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if stage == 0:
                        girl_img = pygame.transform.scale(pygame.image.load(IMAGE_PATHS['TTHEME_GIRL'][chosen_dialogue[2]]), THEME_SIZE)
                        energy_point += chosen_dialogue[3]
                        study_point += chosen_dialogue[4]
                        stage = 1
                    else:
                        run_event = False

        return study_point, energy_point

    def trigger_drink_event(self, health_point, study_point):
        run_event = True
        drink_event_img = pygame.image.load(os.path.join("images/teachertheme", "ttheme_drink.png"))
        drink_event_img = pygame.transform.scale(drink_event_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        dialogue = "你參加了超狂酒局，隔天完全爛掉(健康值-10,讀書進度-10)"

        health_point -= 10
        study_point -= 10

        while run_event:
            self.screen.fill((255, 255, 255))
            img_rect = drink_event_img.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(drink_event_img, img_rect)
            text_surface = self.font_ch.render(dialogue, True, (0, 0, 0))
            self.screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, 100))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    run_event = False

        return health_point, study_point

    def trigger_sleep_event(self, study_point):
        run_event = True
        sleep_event_img = pygame.image.load(os.path.join("images/teachertheme", "ttheme_sleep.png"))
        sleep_event_img = pygame.transform.scale(sleep_event_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        dialogue = "睡太多了吧，不小心在圖書館自習的時候睡著了(讀書進度-10)"

        study_point -= 10

        while run_event:
            self.screen.fill((255, 255, 255))
            img_rect = sleep_event_img.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(sleep_event_img, img_rect)
            text_surface = self.font_ch.render(dialogue, True, (0, 0, 0))
            self.screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, 100))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    run_event = False

        return study_point

    def game_over_screen(self, reason):
        font = pygame.font.Font(FONT_CH_PATH, 30)
        run = True

        if reason == "energy":
            message = "你精力耗盡了，似乎什麼都不重要了"
            image = pygame.image.load(os.path.join("images/ending", "ending_energy0.png"))
        elif reason == "health":
            message = "你身體撐不住，病倒了，但小組報告還是得做"
            image = pygame.image.load(os.path.join("images/ending", "ending_health0.png"))
        elif reason == "graduation":
            message = "恭喜你逃離期末地獄！快樂回家!"
            image = pygame.image.load(os.path.join("images/ending", "ending_study100.png"))
        elif reason == "car":
            message = "你被車撞了，下次記得注意有沒有車暴衝"
            image = pygame.image.load(os.path.join("images/ending", "ending_car.png"))

        image = pygame.transform.scale(image, (733, 400))

        while run:
            self.screen.fill((0, 0, 0))
            self.screen.blit(image, (SCREEN_WIDTH // 2 - 377, 50))
            text = font.render(message, True, (255, 255, 255))
            self.screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 470))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    run = False 