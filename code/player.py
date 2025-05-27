import pygame
from constants import *

class Dinosaur:
    X_pos = 80
    Y_pos = 310
    set_jump_vel = 8.5

    def __init__(self):
        self.run_img = [pygame.transform.scale(pygame.image.load(path), DESIRED_SIZE) for path in IMAGE_PATHS['RUNNING']]
        self.jump_img = pygame.transform.scale(pygame.image.load(IMAGE_PATHS['JUMPING']), DESIRED_SIZE)
        
        self.run_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.step_index = 0
        self.jump_vel = self.set_jump_vel
        
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_pos
        self.dino_rect.y = self.Y_pos
        
        self.start_y = self.Y_pos
        self.max_jump_height = 170
        self.gravity = 0.8
        self.jump_power = 12
        self.short_jump_power = 8

    def update(self, userInput):
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump(userInput)

        if self.step_index >= 20:
            self.step_index = 0

        if userInput[pygame.K_SPACE] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = True
            self.start_y = self.dino_rect.y
            self.jump_vel = self.short_jump_power if not userInput[pygame.K_SPACE] else self.jump_power

        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_run = True
            self.dino_jump = False

    def run(self):
        self.image = self.run_img[self.run_index // 3]
        self.run_index += 1
        if self.run_index >= 9:
            self.run_index = 0
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_pos
        self.dino_rect.y = self.Y_pos
        self.step_index += 1

    def jump(self, userInput):
        self.image = self.jump_img
        if self.dino_jump:
            height_jumped = self.start_y - self.dino_rect.y

            if userInput[pygame.K_SPACE] and self.jump_vel > 0 and height_jumped < self.max_jump_height:
                self.jump_vel -= 0.4
            else:
                self.jump_vel -= self.gravity

            self.dino_rect.y -= self.jump_vel * 1.2

            if self.dino_rect.y >= self.Y_pos:
                self.dino_rect.y = self.Y_pos
                self.dino_jump = False
                self.jump_vel = self.set_jump_vel

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y)) 