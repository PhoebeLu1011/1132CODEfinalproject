import pygame
import random
from constants import *
from player import Dinosaur
from obstacles import Study, Food, Drink, Teacher, Sleep, Car
from events import GameEvents

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(FONT_PATH, 30)
        self.font_ch = pygame.font.Font(FONT_CH_PATH, 20)
        self.events = GameEvents(self.screen)
        
        # 載入圖片
        self.bg = pygame.image.load(IMAGE_PATHS['BG'])
        self.study_images = [pygame.transform.scale(pygame.image.load(path), DESIRED_SIZE) for path in IMAGE_PATHS['STUDY']]
        self.sleep_image = pygame.transform.scale(pygame.image.load(IMAGE_PATHS['SLEEP']), DESIRED_SIZE)
        self.drink_image = pygame.transform.scale(pygame.image.load(IMAGE_PATHS['DRINK']), DESIRED_SIZE)
        self.food_image = pygame.transform.scale(pygame.image.load(IMAGE_PATHS['FOOD']), DESIRED_SIZE)
        self.teacher_image = pygame.transform.scale(pygame.image.load(IMAGE_PATHS['TEACHER']), DESIRED_SIZE)
        self.car_image = pygame.transform.scale(pygame.image.load(IMAGE_PATHS['CAR']), DESIRED_SIZE)
        
        # 初始化玩家
        self.player = Dinosaur()
        self.obstacles = []
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.study_point = INITIAL_STUDY_POINT
        self.energy_point = INITIAL_ENERGY_POINT
        self.health_point = INITIAL_HEALTH_POINT
        self.sleep_count = 0
        self.drink_count = 0
        self.teacher_count = 0
        self.last_health_decrease = pygame.time.get_ticks()

    def reset_game(self):
        self.player = Dinosaur()
        self.obstacles = []
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.study_point = INITIAL_STUDY_POINT
        self.energy_point = INITIAL_ENERGY_POINT
        self.health_point = INITIAL_HEALTH_POINT
        self.sleep_count = 0
        self.drink_count = 0
        self.teacher_count = 0
        self.last_health_decrease = pygame.time.get_ticks()

    def draw_background(self):
        image_width = self.bg.get_width()
        self.screen.blit(self.bg, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(self.bg, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.x_pos_bg = 0
        self.x_pos_bg -= GAME_SPEED

    def draw_score(self):
        text_color = (94, 94, 94)
        study_text = self.font_ch.render(f"讀書進度：{self.study_point}", True, text_color)
        energy_text = self.font_ch.render(f"精力值：{self.energy_point}", True, text_color)
        health_text = self.font_ch.render(f"健康度：{self.health_point}", True, text_color)

        self.screen.blit(study_text, (800, 30))
        self.screen.blit(energy_text, (800, 60))
        self.screen.blit(health_text, (800, 90))

    def handle_collision(self, obstacle):
        if isinstance(obstacle, Study):
            self.study_point += 10
            self.energy_point -= 20
        elif isinstance(obstacle, Sleep):
            self.health_point += 10
            self.energy_point += 5
            self.sleep_count += 1
            if self.sleep_count == 5:
                self.sleep_count = 0
                self.study_point = self.events.trigger_sleep_event(self.study_point)
        elif isinstance(obstacle, Drink):
            self.health_point -= 15
            self.energy_point += 10
            self.drink_count += 1
            if self.drink_count == 5:
                self.drink_count = 0
                self.health_point, self.study_point = self.events.trigger_drink_event(self.health_point, self.study_point)
        elif isinstance(obstacle, Food):
            self.health_point += 5
            self.energy_point += 5
        elif isinstance(obstacle, Teacher):
            self.teacher_count += 1
            self.study_point, self.energy_point = self.events.trigger_teacher_event(self.study_point, self.energy_point)
        elif isinstance(obstacle, Car):
            self.events.game_over_screen("car")
            return True

        # 限制數值範圍
        self.study_point = max(min(self.study_point, 100), 0)
        self.energy_point = max(min(self.energy_point, 100), 0)
        self.health_point = max(min(self.health_point, 100), 0)
        return False

    def run(self):
        self.reset_game()
        run = True

        while run:
            current_time = pygame.time.get_ticks()
            
            # 每秒減少一點健康值
            if current_time - self.last_health_decrease >= HEALTH_DECREASE_INTERVAL:
                self.health_point = max(0, self.health_point - 1)
                self.last_health_decrease = current_time

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.screen.fill((255, 255, 255))
            userInput = pygame.key.get_pressed()

            self.draw_background()
            self.draw_score()

            # 生成障礙物
            if random.random() < 0.1:
                # 檢查是否與現有障礙物距離太近
                can_spawn = True
                for obstacle in self.obstacles:
                    if obstacle.rect.right > SCREEN_WIDTH - 10:  # 如果現有障礙物距離右邊界太近
                        can_spawn = False
                        break

                if can_spawn:
                    r = random.random()
                    if r < 0.03:  # 極低機率生成車子
                        self.obstacles.append(Car(self.car_image))
                    elif r < 0.05:
                        self.obstacles.append(Teacher(self.teacher_image))
                    else:
                        obstacle_type = random.choice(["studying", "sleeping", "drinking", "eating"])
                        if obstacle_type == "studying":
                            self.obstacles.append(Study(self.study_images))
                        elif obstacle_type == "sleeping":
                            self.obstacles.append(Sleep(self.sleep_image))
                        elif obstacle_type == "drinking":
                            self.obstacles.append(Drink(self.drink_image))
                        elif obstacle_type == "eating":
                            self.obstacles.append(Food(self.food_image))

            # 更新和繪製障礙物
            for obstacle in self.obstacles[:]:
                obstacle.draw(self.screen)
                obstacle.update()
                
                # 碰撞檢測
                dino_hitbox = self.player.dino_rect.inflate(-70, -70)
                obstacle_hitbox = obstacle.rect.inflate(-50, -50)
                
                if self.player.dino_rect.colliderect(obstacle_hitbox):
                    if self.handle_collision(obstacle):  # 如果返回 True，表示遊戲結束
                        return
                    self.obstacles.remove(obstacle)

            # 移除超出螢幕的障礙物
            for obstacle in self.obstacles[:]:
                if obstacle.rect.right < 0:
                    self.obstacles.remove(obstacle)

            self.player.draw(self.screen)
            self.player.update(userInput)

            self.clock.tick(30)
            pygame.display.update()

            # 檢查遊戲結束條件
            if self.energy_point <= 0:
                self.events.game_over_screen("energy")
                return
            elif self.health_point <= 0:
                self.events.game_over_screen("health")
                return
            elif self.study_point >= 100:
                self.events.game_over_screen("graduation")
                return

    def menu(self, death_count=0):
        run = True
        while run:
            self.screen.fill((255, 255, 255))
            
            if death_count == 0:
                text = self.font.render("Press any key to start", True, (94, 94, 94))
            else:
                text = self.font.render("Press any key to restart", True, (94, 94, 94))

            textRect = text.get_rect()
            textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            self.screen.blit(text, textRect)
            self.screen.blit(self.player.run_img[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
            
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    self.run() 