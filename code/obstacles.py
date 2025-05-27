import pygame
import random
from constants import *

class Obstacle:
    def __init__(self, image, type):
        self.type = type
        if isinstance(image, list):
            self.image = image[self.type]
        else:
            self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        
    def update(self):
        self.rect.x -= GAME_SPEED
        
    def draw(self, SCREEN):
        SCREEN.blit(self.image, self.rect)

class Study(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = random.randint(70, 310)

class Food(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.randint(70, 310)

class Drink(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.randint(70, 310)

class Teacher(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.randint(70, 310)

class Sleep(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.randint(70, 310)

class Car(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 310  # 固定在地平線上
        self.speed_multiplier = 1.5
    
    def update(self):
        self.rect.x -= GAME_SPEED * self.speed_multiplier  # 使用更快的速度 